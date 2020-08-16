import logging
import os
import pickle
import sys
import time
from collections import OrderedDict
from threading import Event
from typing import Dict

import backtrader as bt
import backtrader.analyzers as btanalyzers
import boto3
import pandas as pd
import quantstats as qs
import simplejson
from backtrader import TimeFrame, num2date

from .analyzers.cash_market import CashMarket
from .configs import BrokerConfig, MarketConfig
from .feeds.utils import get_benchmark
from .feeds.virtual import VirtualFeed
from .utils import build_indicator, build_order

s3 = boto3.client("s3")

# Create logger
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class Strategy(bt.Strategy):
    def __init__(
        self, graph, task_id, interupt_handler: Event = Event(),
    ):
        self.interupt_handler: Event = interupt_handler
        self.task_id = task_id
        self.graph: Dict = dict(
            (constructor["id"], constructor) for constructor in graph
        )
        self.ctx: Dict = dict((data.symbol, dict()) for data in self.datas)
        self.orders: Dict = dict((data.symbol, list()) for data in self.datas)
        self.percent_done: int = 0
        logger.info("Adding node constructors")
        for data in self.datas:
            for constructor in graph:
                self._check_session_aborted()
                if constructor["type"] == "MARKET_NODE":
                    indicator = data
                elif constructor["type"] == "ORDER_NODE":
                    self.orders[data.symbol].append(
                        build_order(self, constructor, self.ctx[data.symbol])
                    )
                elif constructor["type"] == "INDICATOR_NODE":
                    indicator = build_indicator(constructor, self.ctx[data.symbol])
                else:
                    raise ValueError
                self.ctx[data.symbol][constructor["id"]] = indicator
        logger.info("Starting runtime logic")

    def next(self):
        self._check_session_aborted()
        prc = (len(self.data.close) - 1) / len(self.data.close.array)
        if prc - self.percent_done >= 0.1:
            self.percent_done = prc
            logger.info(
                f"Runtime logic completion - {int(self.percent_done * 10) * 10}%"
            )
        for data in self.datas:
            for order in self.orders[data.symbol]:
                order(data)

    def stop(self):
        logger.info("Runtime logic completion - 100%")
        logger.info("Saving nodes to dynamodb")
        for symbol, nodes in self.ctx.items():
            for id, node in nodes.items():
                self._check_session_aborted()
                body = {}
                constructor = self.graph[id]
                for out in constructor["outputs"]:
                    if out == "null":
                        body["null"] = [node[-i] for i in reversed(range(0, len(node)))]
                    else:
                        body[out] = [
                            getattr(node, out)[-i]
                            for i in reversed(range(0, len(node)))
                        ]
                s3.put_object(
                    Body=pickle.dumps(body),
                    Bucket="celery.db",
                    Key=f"nodes/{self.task_id}/{id}/{symbol}",
                )

    def _check_session_aborted(self):
        if self.interupt_handler.is_set():
            raise InterruptedError


def api(
    graph,
    task_id,
    broker_config: BrokerConfig,
    market_config: MarketConfig,
    interupt_handler: Event = Event(),
):
    start_time = time.time()
    try:
        if os.getenv("DEVELOPMENT_MODE"):
            with open("valkyrie-art.txt", "r") as f:
                logger.info(f.read())
                logger.info("DEVELOPMENT MODE")

        cerebro = bt.Cerebro()

        cerebro.addstrategy(
            Strategy, graph=graph, task_id=task_id, interupt_handler=interupt_handler
        )

        configure_market(cerebro, market_config, interupt_handler)
        configure_broker(cerebro, broker_config)
        initial_value = cerebro.broker.getvalue()
        add_analyzers(cerebro)

        # Run and collect strategy
        logger.info("Running cerebro")
        strategies = cerebro.run()
        strat = strategies[0]

        # Get analysis data from cerebro
        sharpe = strat.analyzers.sharperatio.get_analysis()
        returns = strat.analyzers.returns.get_analysis()
        trade_analyzer = strat.analyzers.tradeanalyzer.get_analysis()

        # Setup quantstats session
        qs.extend_pandas()
        cash_market = strat.analyzers.cashmarket.get_analysis()
        df_values = pd.DataFrame(cash_market).T
        df_values = df_values.iloc[:, 1]

        benchmark = get_benchmark(
            market_config.from_date, market_config.to_date, market_config.timeframe
        )
        greeks = qs.stats.greeks(df_values, benchmark)

        # Get transactions and parse for json
        transactions = strat.analyzers.transactions.get_analysis()
        transactions = OrderedDict(
            [(str(date), data) for date, data in transactions.items()]
        )

        # Get position values and parse for json
        positions_value = strat.analyzers.positionsvalue.get_analysis()
        positions_value = OrderedDict(
            [(str(date), data) for date, data in positions_value.items()]
        )

        # Get position sizes and parse for json
        # https://community.backtrader.com/topic/1454/getposition-size-inside-bt-observer
        positions_size = OrderedDict()
        # Header
        positions_size["Datetime"] = list(positions_value["Datetime"])
        prev_date = ""
        index = dict(
            [(symbol, idx) for idx, symbol in enumerate(positions_value["Datetime"])]
        )
        for i, date in enumerate(positions_value.keys()):
            if i == 0:
                # Skip header
                continue
            if i == 1:
                # First tick
                positions_size[date] = [0 for symbol in market_config.symbols]
                prev_date = date
            if i > 1:
                # All following ticks
                positions_size[date] = [v for v in positions_size[prev_date]]
                prev_date = date
            for transaction in transactions.get(date, []):
                size = transaction[0]
                symbol = transaction[3]
                positions_size[date][index[symbol]] += size

        # Get broker data
        broker = {
            "initial_value": initial_value,
            "intermediate_value": [value[1] for value in cash_market.values()],
            "final_value": cerebro.broker.getvalue(),
        }

        logger.info("Saving session to dynamoDB")
        data = {
            "dates": [
                str(num2date(cerebro.datas[0].datetime[-i]))
                for i in reversed(range(0, len(cerebro.datas[0])))
            ],
            "returns": returns,
            "trade_analyzer": simplejson.loads(simplejson.dumps(trade_analyzer)),
            "sharpe": sharpe["sharperatio"],
            "transactions": transactions,
            "broker": broker,
            "positions_value": positions_value,
            "position_size": positions_size,
            "alpha": float(greeks.alpha),  # numpy type
            "beta": float(greeks.beta),  # numpy type
        }

        s3.put_object(
            Body=pickle.dumps(data), Bucket="celery.db", Key=f"sessions/{task_id}"
        )

    except InterruptedError:
        logger.info("Session Aborted")
    logger.info(f"Completed in {time.time() - start_time} seconds")


def configure_market(cerebro, market_config, interupt_handler):
    logger.info("Adding feeds to cerebro")
    for symbol in market_config.symbols:
        feed: VirtualFeed = VirtualFeed(
            symbol=symbol,
            fromdate=market_config.from_date,
            todate=market_config.to_date,
            timeframe=market_config.timeframe,
            interupt_handler=interupt_handler,
        )  # type: ignore
        try:
            feed.virtual_load()
        except StopIteration:
            continue
        cerebro.adddata(feed, name=symbol)


def configure_broker(cerebro, broker_config):
    logger.info("Configuring Broker")
    cerebro.broker.setcash(broker_config.cash)


def add_analyzers(cerebro):
    logger.info("Adding analyzers to cerebro")
    cerebro.addanalyzer(btanalyzers.SharpeRatio, timeframe=bt.TimeFrame.Minutes)
    cerebro.addanalyzer(btanalyzers.Returns, timeframe=bt.TimeFrame.Minutes)
    cerebro.addanalyzer(btanalyzers.Transactions)
    cerebro.addanalyzer(btanalyzers.TradeAnalyzer)
    cerebro.addanalyzer(btanalyzers.PositionsValue, headers=True)
    cerebro.addanalyzer(CashMarket)

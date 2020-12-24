import logging
import os
import pickle
import sys
import time
import traceback
from threading import Event
from typing import Dict

import backtrader as bt
import boto3
from backtrader import TimeFrame, num2date

from .analyzers import add_analyzers, get_analyzers
from .analyzers.cash_market import CashMarket
from .configs import BrokerConfig, MarketConfig, configure_broker, configure_market
from .environ import environ
from .nodes.order.standard_order import market_bracket_order
from .utils import build_indicator, build_order

s3 = boto3.client("s3")

# Create logger
logger = logging.getLogger(__name__)


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
    env: dict = dict(),
):
    environ.update(env)
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
        add_analyzers(cerebro)

        # Run and collect strategy
        logger.info("Running cerebro")
        strategies = cerebro.run(tradehistory=True)

        analyzers = get_analyzers(strategy=strategies[0], market_config=market_config)

        logger.info("Saving session to dynamoDB")
        data = {
            "dates": [
                str(num2date(cerebro.datas[0].datetime[-i]))
                for i in reversed(range(0, len(cerebro.datas[0])))
            ],
            "analyzers": analyzers,
            "elapsed_time": time.time() - start_time,
            "status": "success",
        }
    except InterruptedError:
        logger.info("Session Aborted")
        data = {
            "elapsed_time": time.time() - start_time,
            "status": "aborted",
        }
        raise InterruptedError
    except Exception as e:
        logger.error("Session Failed")
        data = {
            "elapsed_time": time.time() - start_time,
            "status": "failure",
            "traceback": traceback.format_exc(),
            "exception": e,
        }
        logger.error(e)
        logger.error(traceback.format_exc())
        raise e
    s3.put_object(
        Body=pickle.dumps(data), Bucket="celery.db", Key=f"sessions/{task_id}"
    )
    logger.info(f"Completed in {time.time() - start_time} seconds")


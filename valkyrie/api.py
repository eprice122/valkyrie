import logging
import os
import pickle
import sys
import time
import traceback
from threading import Event
from typing import Any, Dict

import backtrader as bt
from backtrader import TimeFrame, num2date

from .analyzers import add_analyzers, get_analyzers
from .analyzers.cash_market import CashMarket
from .configs import BrokerConfig, MarketConfig, configure_broker, configure_market
from .environ import environ
from .nodes.order.standard_order import market_bracket_order
from .utils import build_indicator, build_order, get_market

# Create logger
logger = logging.getLogger(__name__)


class Strategy(bt.Strategy):
    def __init__(
        self, graph, interupt_handler: Event = Event(),
    ):
        self.interupt_handler: Event = interupt_handler
        self.graph = graph
        self.ctx: Dict = dict((data.symbol, dict()) for data in self.datas)
        self.orders: Dict = dict((data.symbol, list()) for data in self.datas)
        self.percent_done: int = 0
        logger.info("Adding node constructors")
        for data in self.datas:
            for constructor in self.graph.values():
                self._check_session_aborted()
                if constructor["type"] == "MARKET_NODE":
                    indicator = data
                elif constructor["type"] == "ORDER_NODE":
                    self.orders[data.symbol].append(
                        build_order(self, constructor, self.ctx[data.symbol])
                    )
                elif constructor["type"] == "INDICATOR_NODE":
                    indicator = build_indicator(
                        strategy=self,
                        data=data,
                        constructor=constructor,
                        nodes=self.ctx[data.symbol],
                    )
                else:
                    raise ValueError
                self.ctx[data.symbol][constructor["id"]] = indicator
        logger.info("Starting runtime logic")

    def prenext(self):
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

    def _check_session_aborted(self):
        if self.interupt_handler.is_set():
            raise InterruptedError


def api(
    graph,
    task_id: str,
    broker_config: BrokerConfig,
    market_config: MarketConfig,
    interupt_handler: Event = Event(),
    env: dict = dict(),
):
    graph = dict((constructor["id"], constructor) for constructor in graph)

    environ.update(env)
    execution_time = time.time()
    data: Dict[str, Any] = dict(
        {
            "execution_time": execution_time,
            "id": task_id,
            "symbols": market_config.symbols,
        }
    )
    try:
        cerebro: bt.Cerebro = bt.Cerebro()

        cerebro.addstrategy(Strategy, graph=graph, interupt_handler=interupt_handler)

        configure_market(cerebro, market_config, interupt_handler)
        configure_broker(cerebro, broker_config)
        add_analyzers(cerebro)

        # Run and collect strategy
        logger.info("Running cerebro")
        strategies = cerebro.run(tradehistory=True)

        analyzers = get_analyzers(strategy=strategies[0], market_config=market_config)

        data["market"] = get_market(cerebro)

        completion_time = time.time()
        data["dates"] = [
            str(num2date(cerebro.datas[0].datetime[-i]))
            for i in reversed(range(0, len(cerebro.datas[0])))
        ]

        ctx = strategies[0].ctx
        results: Dict[str, Dict[str, Dict[str, list]]] = dict()
        for symbol, nodes in ctx.items():
            results[symbol] = dict()
            for id, node in nodes.items():
                if interupt_handler.is_set():
                    raise InterruptedError
                body = dict()
                constructor = graph[id]
                for out in constructor["outputs"]:
                    if out == "null":
                        body["null"] = [node[-i] for i in reversed(range(0, len(node)))]
                    else:
                        body[out] = [
                            getattr(node, out)[-i]
                            for i in reversed(range(0, len(node)))
                        ]
                results[symbol][id] = body

        data["results"] = results
        data["analyzers"] = analyzers
        data["node_ids"] = [node["id"] for node in graph.values()]

    except InterruptedError:
        logger.info("Session Aborted")
        raise InterruptedError
    except Exception as e:
        logger.error("Session Failed")
        error = dict()
        error["traceback"] = traceback.format_exc()
        error["message"] = str(e)
        data["error"] = error
        logger.error(e)
        logger.error(traceback.format_exc())
        raise e

    completion_time = time.time()
    data["completion_time"] = completion_time

    logger.info(f"Completed in {completion_time - execution_time} seconds")
    return data

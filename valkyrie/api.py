import logging
import os
import sys
from threading import Event
from typing import Dict

import backtrader as bt
import backtrader.feeds as btfeeds
import backtrader.indicators as btind
import boto3
import simplejson
from backtrader import num2date

from .configs import BrokerConfig, MarketConfig
from .feeds.mongo import MongoFeed
from .feeds.virtual import VirtualFeed
from .utils import build_beacon, build_indicator

dynamodb = boto3.resource("dynamodb")
sessions_table = dynamodb.Table("celerySessions")
node_table = dynamodb.Table("celeryNodes")
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
        self.ctx: Dict = dict((data._name, dict()) for data in self.datas)
        self.orders = list()
        for data in self.datas:
            symbol = data._name
            for constructor in graph:
                if constructor["type"] == "MARKET_NODE":
                    indicator = self.data
                elif constructor["type"] == "ORDER_NODE":
                    self.orders.append(
                        build_beacon(self, constructor, self.ctx[symbol])
                    )
                elif constructor["type"] == "INDICATOR_NODE":
                    indicator = build_indicator(constructor, self.ctx[symbol])
                else:
                    raise ValueError
                self.ctx[symbol][constructor["id"]] = indicator

        self.bb = btind.BollingerBands(self.data)
        self.test = self.data.close - self.data.open

    def next(self):
        if self.interupt_handler.is_set():
            self.env.runstop()
        for data in self.datas:
            # self.buy(data=data, size=100,)
            dt, dn = self.datetime.date(), data._name
            pos = self.getposition(data).size
            for order in self.orders:
                order(data)

    def stop(self):
        for symbol, nodes in self.ctx.items():
            for id, node in nodes.items():
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
                node_table.put_item(
                    Item={
                        "task_id": self.task_id,
                        "node_id": f"{symbol}#{id}",
                        "data": simplejson.dumps(body, use_decimal=True),
                    }
                )
        # Put session properties
        sessions_table.put_item(
            Item={
                "task_id": self.task_id,
                "dates": [
                    str(num2date(self.data.datetime[-i]))
                    for i in reversed(range(0, len(node)))
                ],
            }
        )


def api(
    graph,
    task_id,
    broker_config: BrokerConfig,
    market_config: MarketConfig,
    interupt_handler: Event = Event(),
):
    if os.getenv("DEVELOPMENT_MODE"):
        with open("valkyrie-art.txt", "r") as f:
            logger.info(f.read())

    cerebro = bt.Cerebro()
    cerebro.addstrategy(
        Strategy, graph=graph, task_id=task_id, interupt_handler=interupt_handler
    )
    for symbol in market_config.symbols:
        feed: VirtualFeed = VirtualFeed(
            symbol=symbol,
            fromdate=market_config.from_date,
            todate=market_config.to_date,
            timeframe=market_config.timeframe,
        )  # type: ignore
        try:
            feed.virtual_load()
        except StopIteration:
            continue
        cerebro.adddata(feed, name=symbol)

    cerebro.broker.setcash(broker_config.cash)
    print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
    cerebro.run()
    print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

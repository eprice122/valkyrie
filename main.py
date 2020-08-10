from datetime import datetime

import backtrader as bt
import backtrader.feeds as btfeeds
import backtrader.indicators as btind

from valkyrie.api import api
from valkyrie.configs import BrokerConfig, MarketConfig
from valkyrie.feeds.mongo import MongoFeed
from valkyrie.utils import build_indicator

d = [
    {
        "node_str": "market",
        "module_str": "market",
        "id": "642e8a47-e1c4-4273-b580-61522e27273c",
        "type": "MARKET_NODE",
        "parameters": {},
        "inputs": {},
        "outputs": ["open", "high", "low", "close", "volume"],
    },
    {
        "node_str": "comparator",
        "module_str": "fundamental",
        "id": "1ad7ee9c-a16c-4254-a0e9-37488664549f",
        "type": "INDICATOR_NODE",
        "parameters": {"logic": 0},
        "inputs": {
            "input1": {
                "value": [
                    {
                        "port_id": "close",
                        "node_id": "642e8a47-e1c4-4273-b580-61522e27273c",
                    }
                ],
                "key": "input1",
                "multi": False,
            },
            "input0": {
                "value": [
                    {
                        "port_id": "open",
                        "node_id": "642e8a47-e1c4-4273-b580-61522e27273c",
                    }
                ],
                "key": "input0",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
    {
        "node_str": "market_order",
        "module_str": "standard_order",
        "id": "1ad2ee9c-a46c-4254-a0e9-37422664549f",
        "type": "ORDER_NODE",
        "parameters": {"size": 10, "side": "BUY", "price": 1.02},
        "inputs": {
            "inp": {
                "value": [
                    {
                        "port_id": "null",
                        "node_id": "1ad7ee9c-a16c-4254-a0e9-37488664549f",
                    }
                ],
                "key": "inp",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
]


class Strategy(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        # print("%s, %s" % (dt.isoformat(), txt))

    def __init__(self):
        self.d = self.data.close - self.data.close(-2)

    def next(self):
        self.log("Close, %.2f" % self.data.close[0])

    def stop(self):
        x = 0


if __name__ == "__main__":
    import time

    start = time.time()

    api(
        d,
        market_config=MarketConfig(
            from_date=datetime(year=2014, month=1, day=1),
            to_date=datetime(year=2014, month=1, day=10),
            timeframe=bt.TimeFrame.Minutes,
            symbols={"A", "AAPL", "F"},
        ),
        broker_config=BrokerConfig(cash=100_000),
        task_id="myId",
    )

    end = time.time()
    print(end - start)

    x = 0

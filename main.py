from datetime import datetime

import backtrader as bt

from valkyrie.api import api
from valkyrie.configs import BrokerConfig, MarketConfig

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
        "node_str": "node_comparator",
        "module_str": "fundamental",
        "id": "1ad7ee9c-a16c-4254-a0e9-37488664549f",
        "type": "INDICATOR_NODE",
        "parameters": {"logic": 0},
        "inputs": {
            "input0": {
                "value": [
                    {
                        "port_id": "close",
                        "node_id": "642e8a47-e1c4-4273-b580-61522e27273c",
                    },
                ],
                "key": "input0",
                "multi": False,
            },
            "input1": {
                "value": [
                    {
                        "port_id": "open",
                        "node_id": "642e8a47-e1c4-4273-b580-61522e27273c",
                    },
                ],
                "key": "input1",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
    {
        "node_str": "market_bracket_order",
        "module_str": "standard_order",
        "id": "1ad2ee9c-a46c-4254-a0e9-37422664549f",
        "type": "ORDER_NODE",
        "parameters": {
            "size": 10,
            "side": "BUY",
            "upper_type": 0,
            "upper_trigger": 1,
            "lower_type": 1,
            "lower_trigger": -1,
        },
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


if __name__ == "__main__":
    api(
        d,
        market_config=MarketConfig(
            from_date=datetime(year=2014, month=1, day=1),
            to_date=datetime(year=2014, month=1, day=4),
            timeframe=bt.TimeFrame.Minutes,
            symbols=["F", "AAPL"],
        ),
        broker_config=BrokerConfig(cash=100_000_000),
        task_id="myId",
    )

import logging
import os
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
        "node_str": "crossover",
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
                        "port_id": "high",
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
        "node_str": "math",
        "module_str": "fundamental",
        "id": "2",
        "type": "INDICATOR_NODE",
        "parameters": {"logic": 1},
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
        "node_str": "lookback",
        "module_str": "fundamental",
        "id": "6",
        "type": "INDICATOR_NODE",
        "parameters": {"period": 20},
        "inputs": {
            "input0": {
                "value": [
                    {
                        "port_id": "If",
                        "node_id": "1ad7ee9c-a16c-4254-a0e9-37488664549f",
                    },
                ],
                "key": "input0",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
    {
        "node_str": "default_value",
        "module_str": "fundamental",
        "id": "36",
        "type": "INDICATOR_NODE",
        "parameters": {"value": 15},
        "inputs": {
            "input0": {
                "value": [{"port_id": "null", "node_id": "6",},],
                "key": "input0",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
    {
        "node_str": "accumulate",
        "module_str": "fundamental",
        "id": "0",
        "type": "INDICATOR_NODE",
        "parameters": {},
        "inputs": {
            "input0": {
                "value": [{"port_id": "null", "node_id": "2",},],
                "key": "input0",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
    {
        "node_str": "cci",
        "module_str": "momentum",
        "id": "5",
        "type": "INDICATOR_NODE",
        "parameters": {"period": 15},
        "inputs": {},
        "outputs": ["null"],
    },
    {
        "node_str": "market_order",
        "module_str": "standard_order",
        "id": "1",
        "type": "ORDER_NODE",
        "parameters": {"size": 10, "side": "BUY",},
        "inputs": {
            "input0": {
                "value": [
                    {
                        "port_id": "If",
                        "node_id": "1ad7ee9c-a16c-4254-a0e9-37488664549f",
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
        "id": "76",
        "type": "ORDER_NODE",
        "parameters": {"size": 10, "side": "SELL",},
        "inputs": {
            "input0": {
                "value": [{"port_id": "null", "node_id": "6",}],
                "key": "input0",
                "multi": False,
            },
        },
        "outputs": ["null"],
    },
    # {
    #     "node_str": "market_bracket_order",
    #     "module_str": "standard_order",
    #     "id": "1",
    #     "type": "ORDER_NODE",
    #     "parameters": {
    #         "size": 10,
    #         "side": "BUY",
    #         "upper_type": 0,
    #         "upper_trigger": 1,
    #         "lower_type": 1,
    #         "lower_trigger": -1,
    #     },
    #     "inputs": {
    #         "input0": {
    #             "value": [
    #                 {
    #                     "port_id": "If",
    #                     "node_id": "1ad7ee9c-a16c-4254-a0e9-37488664549f",
    #                 }
    #             ],
    #             "key": "inp",
    #             "multi": False,
    #         },
    #     },
    #     "outputs": ["null"],
    # },
]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    results = api(
        d,
        market_config=MarketConfig(
            from_date=datetime(year=2014, month=1, day=1),
            to_date=datetime(year=2014, month=1, day=4),
            timeframe=bt.TimeFrame.Minutes,
            symbols=["F", "AAPL"],
        ),
        broker_config=BrokerConfig(cash=100_000_000),
        task_id="myId",
        env={
            "MONGO_HOST": os.environ["MONGO_HOST"],
            "MONGO_PORT": os.environ["MONGO_PORT"],
            "MONGO_MARKET_USER": os.environ["MONGO_MARKET_USER"],
            "MONGO_MARKET_PWD": os.environ["MONGO_MARKET_PWD"],
        },
    )


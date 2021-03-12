from datetime import datetime
from typing import List
from unittest import TestCase
from uuid import uuid4

from .api_utils import use_api, use_market_node

_MARKET_ID = uuid4()


class TestFunctional(TestCase):
    def test_functional_0(self):
        market = use_market_node(_MARKET_ID)
        sma_node = {
            "node_str": "simple_moving_average",
            "module_str": "average",
            "id": uuid4(),
            "type": "INDICATOR_NODE",
            "parameters": {"period": 10},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        cross0_node = {
            "node_str": "crossover",
            "module_str": "fundamental",
            "id": "cross0",
            "type": "INDICATOR_NODE",
            "parameters": {"logic": 0},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
                "input1": {
                    "value": [{"port_id": "open", "node_id": _MARKET_ID,},],
                    "key": "input1",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        cross1_node = {
            "node_str": "crossover",
            "module_str": "fundamental",
            "id": "cross1",
            "type": "INDICATOR_NODE",
            "parameters": {"logic": 0},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "open", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
                "input1": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input1",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        order0_node = {
            "node_str": "market_order",
            "module_str": "standard_order",
            "id": uuid4(),
            "type": "ORDER_NODE",
            "parameters": {"side": "BUY", "size": 10,},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "null", "node_id": "cross0",},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        order1_node = {
            "node_str": "market_order",
            "module_str": "standard_order",
            "id": uuid4(),
            "type": "ORDER_NODE",
            "parameters": {"side": "SELL",},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "null", "node_id": "cross1",},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        results = use_api(
            [market, cross0_node, cross1_node, order0_node, order1_node,],
        )

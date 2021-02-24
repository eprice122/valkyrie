from datetime import datetime
from typing import List
from unittest import TestCase
from uuid import uuid4

from .api_utils import use_api, use_market_node

_MODULE_NAME = "extrema"
_MODULE_TYPE = "INDICATOR_NODE"
_MARKET_ID = uuid4()


class TestExtrema(TestCase):
    def test_lowest_value(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "lowest_value",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"period": 3},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        results = use_api([market, node])

    def test_highest_value(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "highest_value",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"period": 3},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        results = use_api([market, node])

    def test_lowest_index(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "lowest_index",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"period": 3},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }

        results = use_api([market, node])

    def test_highest_index(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "highest_index",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"period": 3},
            "inputs": {
                "input0": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "input0",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }

        results = use_api([market, node])

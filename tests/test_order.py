from datetime import datetime
from typing import List
from unittest import TestCase
from uuid import uuid4

from .api_utils import use_api, use_market_node

_MODULE_NAME = "standard_order"
_MODULE_TYPE = "ORDER_NODE"
_MARKET_ID = uuid4()


class TestOrder(TestCase):
    def test_market_order(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "market_order",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"side": "BUY", "size": 10,},
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

    def test_stop_order(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "stop_order",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"side": "BUY", "size": 10, "trigger_percent": 1,},
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

    def test_limit_order(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "limit_order",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"side": "BUY", "size": 10, "limit_percent": 1,},
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

    def test_stop_limit_order(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "stop_limit_order",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {
                "side": "BUY",
                "size": 10,
                "limit_percent": 1,
                "trigger_percent": 1,
            },
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

    def test_stop_trail(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "stop_trail",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"side": "BUY", "size": 10, "trail_percent": -1,},
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

    def test_market_bracket_order(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "market_bracket_order",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {
                "side": "BUY",
                "size": 10,
                "upper_type": 0,
                "lower_type": 0,
                "upper_trigger": 2,
                "lower_trigger": -1,
            },
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

    def test_limit_bracket_order(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "limit_bracket_order",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {
                "side": "BUY",
                "size": 10,
                "upper_type": 0,
                "lower_type": 0,
                "upper_trigger": 1,
                "middle_trigger": 1,
                "lower_trigger": -1,
            },
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


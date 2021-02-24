from datetime import datetime
from typing import List
from unittest import TestCase
from uuid import uuid4

from .api_utils import use_api, use_market_node

_MODULE_NAME = "average"
_MODULE_TYPE = "INDICATOR_NODE"
_MARKET_ID = uuid4()


class TestAverage(TestCase):
    def test_simple_moving_average(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "simple_moving_average",
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

    def test_sma_env(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "sma_env",
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

    def test_exponential_moving_average(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "exponential_moving_average",
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

    def test_triple_ema(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "triple_ema",
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

    def test_weighted_moving_average(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "weighted_moving_average",
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

    def test_average_true_range(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "average_true_range",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"period": 3},
            "inputs": {
                "high": {
                    "value": [{"port_id": "high", "node_id": _MARKET_ID,},],
                    "key": "high",
                    "multi": False,
                },
                "low": {
                    "value": [{"port_id": "low", "node_id": _MARKET_ID,},],
                    "key": "low",
                    "multi": False,
                },
                "close": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "close",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }

        results = use_api([market, node])

    def test_true_range(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "true_range",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {},
            "inputs": {
                "high": {
                    "value": [{"port_id": "high", "node_id": _MARKET_ID,},],
                    "key": "high",
                    "multi": False,
                },
                "low": {
                    "value": [{"port_id": "low", "node_id": _MARKET_ID,},],
                    "key": "low",
                    "multi": False,
                },
                "close": {
                    "value": [{"port_id": "close", "node_id": _MARKET_ID,},],
                    "key": "close",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }

        results = use_api([market, node])


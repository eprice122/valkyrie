from datetime import datetime
from typing import List
from unittest import TestCase
from uuid import uuid4

from .api_utils import use_api, use_market_node

_MODULE_NAME = "momentum"
_MODULE_TYPE = "INDICATOR_NODE"
_MARKET_ID = uuid4()


class TestMomentum(TestCase):
    def test_bollinger_bands(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "bollinger_bands",
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

    def test_cci(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "cci",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"period": 3},
            "inputs": {},
            "outputs": ["null"],
        }
        results = use_api([market, node])

    def test_derivative(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "derivative",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {},
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

    def test_macd(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "macd",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {},
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

    def test_rsi(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "rsi",
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

    def test_rate_of_change(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "rate_of_change",
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

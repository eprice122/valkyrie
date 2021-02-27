from datetime import datetime
from typing import List
from unittest import TestCase
from uuid import uuid4

from .api_utils import use_api, use_market_node

_MODULE_NAME = "fundamental"
_MODULE_TYPE = "INDICATOR_NODE"
_MARKET_ID = uuid4()


class TestFundamental(TestCase):
    def test_switch(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "switch",
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
                "state": {
                    "value": [{"port_id": "open", "node_id": _MARKET_ID,},],
                    "key": "state",
                    "multi": False,
                },
            },
            "outputs": ["null"],
        }
        results = use_api([market, node])

    def test_sum_n(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "sum_n",
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

    def test_rank(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "rank",
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

    def test_or_logic(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "or_logic",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {},
            "inputs": {
                "inputs": {
                    "value": [
                        {"port_id": "close", "node_id": _MARKET_ID,},
                        {"port_id": "open", "node_id": _MARKET_ID,},
                    ],
                    "key": "inputs",
                    "multi": True,
                },
            },
            "outputs": ["null"],
        }

        results = use_api([market, node])

    def test_and_logic(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "and_logic",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {},
            "inputs": {
                "inputs": {
                    "value": [
                        {"port_id": "close", "node_id": _MARKET_ID,},
                        {"port_id": "open", "node_id": _MARKET_ID,},
                    ],
                    "key": "inputs",
                    "multi": True,
                },
            },
            "outputs": ["null"],
        }

        results = use_api([market, node])

    def test_math(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "math",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
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

        results = use_api([market, node])

    def test_lookback(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "lookback",
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

    def test_default_value(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "default_value",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"value": 3},
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

    def test_crossover(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "crossover",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
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

        results = use_api([market, node])

    def test_constant(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "constant",
            "module_str": _MODULE_NAME,
            "id": uuid4(),
            "type": _MODULE_TYPE,
            "parameters": {"value": 3},
            "inputs": {},
            "outputs": ["null"],
        }

        results = use_api([market, node])

    def test_any_n(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "any_n",
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

    def test_all_n(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "all_n",
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

    def test_accumulate(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "accumulate",
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

    def test_absolute_value(self):
        market = use_market_node(_MARKET_ID)
        node = {
            "node_str": "absolute_value",
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

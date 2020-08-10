import json
from typing import List, Optional

# Node Types
MARKET_NODE = "MARKET_NODE"
INDICATOR_NODE = "INDICATOR_NODE"
ASSESS_NODE = "ASSESS_NODE"
BROKER_NODE = "BROKER_NODE"

UI_INT = "UI_INT"
UI_FLOAT = "UI_FLOAT"
UI_STRING = "UI_STRING"
UI_BOOL = "UI_BOOL"
UI_SELECTOR = "UI_SELECTOR"


class Color:
    def __init__(self, red: int, green: int, blue: int):
        assert 0 <= red < 256
        assert 0 <= green < 256
        assert 0 <= blue < 256
        self.red = red
        self.green = green
        self.blue = blue


class Constraints:
    def __init__(
        self,
        lower_bound: float = None,
        upper_bound: float = None,
        not_zero: bool = False,
    ):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.not_zero = not_zero


class UI:
    def __init__(self, type, default):
        self.type = type
        self.default = default


class IntegerUI(UI):
    def __init__(self, constraints: Constraints = None, default: Optional[int] = None):
        super().__init__(type=UI_INT, default=default)
        self.constraints = constraints


class FloatUI(UI):
    def __init__(self, constraints: Constraints = None, default: Optional[int] = None):
        super().__init__(type=UI_FLOAT, default=default)
        self.constraints = constraints


class StringUI(UI):
    def __init__(self, constraints: Constraints = None, default: Optional[int] = None):
        super().__init__(type=UI_STRING, default=default)
        self.constraints = constraints


class SelectorUI(UI):
    def __init__(self, options: dict = {}, default=None):
        super().__init__(type=UI_SELECTOR, default=default)
        self.options = options


class Parameter:
    def __init__(self, key: str, label: str, ui: UI):
        self.key = key
        self.label = label
        self.ui = ui


class Input:
    def __init__(
        self,
        key: str,
        label: str = "Input",
        constraints: List[str] = [MARKET_NODE, INDICATOR_NODE],
        multi: bool = False,
    ):
        self.key = key
        self.label = label
        self.multi = multi
        self.constraints = constraints


class Output:
    def __init__(self, label: str = "Output", key: str = None):
        self.label = label
        self.key = key


class Node:
    def __init__(
        self,
        key: str,
        label: str,
        type: str,
        tooltip: str,
        docs_path: str,
        parameters: List[Parameter],
        inputs: List[Input],
        outputs: List[Output],
    ):
        self.key = key
        self.label = label
        self.type = type
        self.tooltip = tooltip
        self.docs_path = docs_path
        self.parameters = parameters
        self.inputs = inputs
        self.outputs = outputs


class Module:
    def __init__(
        self, key: str, label: str, color: Color, icon: str, nodes: List[Node]
    ):
        self.key = key
        self.label = label
        self.color = color
        self.icon = icon
        self.nodes = nodes

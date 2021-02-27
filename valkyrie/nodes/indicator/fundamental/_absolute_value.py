import math

import backtrader as bt
import backtrader.indicators as btind

from ...entities import FloatUI, Input, IntegerUI, Node, Output, Parameter

absolute_value_docs = Node(
    key="absolute_value",
    label="Absolute Value",
    type="INDICATOR_NODE",
    tooltip="Outputs the absolute value of the input.",
    docs_path="absolute_value.md",
    parameters=[],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def absolute_value(input0):
    return abs(input0)

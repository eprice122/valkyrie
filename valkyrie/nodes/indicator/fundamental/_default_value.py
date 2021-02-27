import math

import backtrader as bt
import backtrader.indicators as btind

from ...entities import FloatUI, Input, IntegerUI, Node, Output, Parameter

default_value_docs = Node(
    key="default_value",
    label="Default Value",
    type="INDICATOR_NODE",
    tooltip="Allows user to default nan values to a constant.",
    docs_path="default_value.md",
    parameters=[Parameter(key="value", label="Value", ui=FloatUI()),],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


class DefaultValue(bt.Indicator):
    lines = ("default",)

    def __init__(self, input0, value):
        self.input0 = input0
        self.value = value

    def next(self):
        inp0 = self.input0.array
        dst = self.array
        dst[i] = self.value if math.isnan(inp0[0]) else inp0[0]

    def once(self, start, end):
        # cache python dictionary lookups
        dst = self.array
        inp0 = self.input0.array

        for i in range(start, end):
            dst[i] = self.value if math.isnan(inp0[i]) else inp0[i]


def default_value(input0, value):
    return DefaultValue(input0=input0, value=value)

import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

derivative_docs = Node(
    key="derivative",
    label="Derivative",
    type="INDICATOR_NODE",
    tooltip="Takes the derivative of line in respect to the period length.",
    docs_path="derivative.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI(default=1))],
    inputs=[Input(key="input0", label="Input",)],
    outputs=[Output()],
)


def derivative(input0, period):
    return input0(0) - input0(-period)

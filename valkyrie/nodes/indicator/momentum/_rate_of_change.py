import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

rate_of_change_docs = Node(
    key="rate_of_change",
    label="Rate of Change",
    type="INDICATOR_NODE",
    tooltip="Measures the ratio of change in prices over a period.",
    docs_path="rate_of_change.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def rate_of_change(input0, period):
    return btind.RateOfChange(input0, period=period)


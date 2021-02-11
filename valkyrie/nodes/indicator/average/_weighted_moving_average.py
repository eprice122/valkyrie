import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

weighted_moving_average_docs = Node(
    key="weighted_moving_average",
    label="Weighted Moving Average",
    type="INDICATOR_NODE",
    tooltip="A Moving Average which gives an arithmetic weighting to values with the newest having the more weight.",
    docs_path="weighted_moving_average.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def weighted_moving_average(inp, period):
    return btind.WeightedMovingAverage(inp, period=period)

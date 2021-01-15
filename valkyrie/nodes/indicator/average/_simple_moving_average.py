import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

simple_moving_average_docs = Node(
    key="simple_moving_average",
    label="Simple Moving Average",
    type="INDICATOR_NODE",
    tooltip="Non-weighted average of the last n periods.",
    docs_path="simple_moving_average.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def simple_moving_average(inp, period):
    return btind.MovingAverageSimple(inp, period=period)

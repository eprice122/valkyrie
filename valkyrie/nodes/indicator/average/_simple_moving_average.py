import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

simple_moving_average_docs = Node(
    key="simple_moving_average",
    label="Simple Moving Average",
    type="INDICATOR_NODE",
    tooltip="Non-weighted average of the last n periods.",
    docs_path="simple_moving_average.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)


def simple_moving_average(input0, period):
    return btind.MovingAverageSimple(input0, period=period)

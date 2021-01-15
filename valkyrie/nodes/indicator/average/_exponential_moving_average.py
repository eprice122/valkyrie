import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

exponential_moving_average_docs = Node(
    key="exponential_moving_average",
    label="Exponential Moving Average",
    type="INDICATOR_NODE",
    tooltip="A Moving Average that smoothes data exponentially over time.",
    docs_path="exponential_moving_average.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def exponential_moving_average(inp, period):
    return btind.ExponentialMovingAverage(inp, period=period)


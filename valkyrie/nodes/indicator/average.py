import backtrader.indicators as btind

from ..entities import (
    Color,
    Input,
    IntegerUI,
    Module,
    Node,
    Output,
    Parameter,
    SelectorUI,
)

simple_moving_average_docs = Node(
    key="simple_moving_average",
    label="Simple Moving Average",
    type="INDICATOR_NODE",
    tooltip="Non-weighted average of the last n periods",
    docs_path="simple_moving_average.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def simple_moving_average(inp, period):
    return btind.MovingAverageSimple(inp, period=period)


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
    return btind.WeightedAverage(inp, period=period)


average_docs = Module(
    key="average",
    label="Average",
    color=Color(red=197, green=17, blue=98),
    icon="fas fa-snowplow",
    nodes=[
        simple_moving_average_docs,
        exponential_moving_average_docs,
        weighted_moving_average_docs,
    ],
)

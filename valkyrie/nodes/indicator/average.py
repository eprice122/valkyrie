import backtrader.indicators as btind

from ..entities import (Color, Input, IntegerUI, Module, Node, Output,
                        Parameter, SelectorUI)

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


true_range_docs = Node(
    key="true_range",
    label="True Range",
    type="INDICATOR_NODE",
    tooltip="Gauges the volatility of the market during each tick.",
    docs_path="true_range.md",
    parameters=[],
    inputs=[
        Input(key="high", label="High"),
        Input(key="low", label="Low"),
        Input(key="close", label="Close"),
    ],
    outputs=[Output(label="Output")],
)


def true_range(high, low, close):
    return btind.Max(abs(high - low), abs(high - close), abs(low - close))


average_true_range_docs = Node(
    key="average_true_range",
    label="Average True Range",
    type="INDICATOR_NODE",
    tooltip="Average volatility of the market during each tick.",
    docs_path="average_true_range.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[
        Input(key="high", label="High"),
        Input(key="low", label="Low"),
        Input(key="close", label="Close"),
    ],
    outputs=[Output(label="Output")],
)


def average_true_range(high, low, close, period):
    tr = true_range(high, low, close)
    return btind.MovingAverageSimple(tr, period=period)


average_docs = Module(
    key="average",
    label="Average",
    color=Color(red=197, green=17, blue=98),
    icon="fas fa-snowplow",
    nodes=[
        simple_moving_average_docs,
        exponential_moving_average_docs,
        weighted_moving_average_docs,
        true_range_docs,
    ],
)

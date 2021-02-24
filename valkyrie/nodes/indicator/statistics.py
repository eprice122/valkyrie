import backtrader.indicators as btind

from ..entities import Color, Input, IntegerUI, Module, Node, Output, Parameter

standard_deviation_docs = Node(
    key="standard_deviation",
    label="Standard Deviation",
    type="INDICATOR_NODE",
    tooltip="Measures the spread of the stock prices.",
    docs_path="standard_deviation.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI(),)],
    inputs=[Input(key="input0", label="Input",)],
    outputs=[Output(label="Output")],
)


def standard_deviation(input0, period):
    return btind.StandardDeviation(input0, period=period)


mean_deviation_docs = Node(
    key="mean_deviation",
    label="Mean Deviation",
    type="INDICATOR_NODE",
    tooltip="The average absolute difference each value is from the period's mean.",
    docs_path="mean_deviation.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI(),)],
    inputs=[Input(key="input0", label="Input",)],
    outputs=[Output(label="Output")],
)


def mean_deviation(input0, period):
    return btind.MeanDeviation(input0, period=period)


statistics_module = Module(
    key="statistics",
    label="Statistics",
    color=Color(red=135, green=168, blue=50),
    icon="fas fa-chart-bar",
    nodes=[mean_deviation_docs, standard_deviation_docs],
)

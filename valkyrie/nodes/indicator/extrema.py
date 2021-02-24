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

lowest_value_docs = Node(
    key="lowest_value",
    label="Lowest Value",
    type="INDICATOR_NODE",
    tooltip="The lowest value for the data in a given period.",
    docs_path="lowest_value.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)


def lowest_value(input0, period):
    return btind.Lowest(input0, period=period)


highest_value_docs = Node(
    key="highest_value",
    label="Highest Value",
    type="INDICATOR_NODE",
    tooltip="The highest value for the data in a given period.",
    docs_path="highest_value.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)


def highest_value(input0, period):
    return btind.Highest(input0, period=period)


lowest_index_docs = Node(
    key="lowest_index",
    label="Lowest Index",
    type="INDICATOR_NODE",
    tooltip="Returns the index of the first data that is the lowest in the period.",
    docs_path="lowest_index.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)


def lowest_index(input0, period):
    return btind.FindFirstIndexLowest(input0, period=period)


highest_index_docs = Node(
    key="highest_index",
    label="Highest Index",
    type="INDICATOR_NODE",
    tooltip="Returns the index of the first data that is the highest in the period.",
    docs_path="highest_index.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)


def highest_index(input0, period):
    return btind.FindFirstIndexHighest(input0, period=period)


extrema_docs = Module(
    key="extrema",
    label="Extrema",
    color=Color(red=77, green=182, blue=172),
    icon="fas fa-sort",
    nodes=[
        lowest_value_docs,
        highest_value_docs,
        lowest_index_docs,
        highest_index_docs,
    ],
)

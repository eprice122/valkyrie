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
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def lowest_value(inp, period):
    return btind.Lowest(inp, period=period)


highest_value_docs = Node(
    key="highest_value",
    label="Highest Value",
    type="INDICATOR_NODE",
    tooltip="The highest value for the data in a given period.",
    docs_path="highest_index.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def highest_value(inp, period):
    return btind.Lowest(inp, period=period)


lowest_index_docs = Node(
    key="lowest_index",
    label="Lowest Index",
    type="INDICATOR_NODE",
    tooltip="Returns the index of the first data that is the lowest in the period.",
    docs_path="lowest_index.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def lowest_index(inp, period):
    return btind.Lowest(inp, period=period)


highest_index_docs = Node(
    key="highest_index",
    label="Highest Index",
    type="INDICATOR_NODE",
    tooltip="Returns the index of the first data that is the highest in the period.",
    docs_path="highest_index.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def highest_index(inp, period):
    return btind.index(inp, period=period)


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

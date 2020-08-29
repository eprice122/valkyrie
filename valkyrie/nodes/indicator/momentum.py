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

commodity_channel_index_docs = Node(
    key="commodity_channel_index",
    label="Commodity Channel Index",
    type="INDICATOR_NODE",
    tooltip="Measures variations of the “typical price” from its mean to identify extremes and reversals.",
    docs_path="commodity_channel_index.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[],
    outputs=[Output()],
)


def commodity_channel_index(period: int):
    return btind.CommodityChannelIndex(period=period)


rate_of_change_docs = Node(
    key="rate_of_change",
    label="Rate of Change",
    type="INDICATOR_NODE",
    tooltip="Measures the ratio of change in prices over a period.",
    docs_path="rate_of_change.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output()],
)


def rate_of_change(inp, period):
    return btind.RateOfChange(inp, period=period, safediv=True)


rsi_docs = Node(
    key="rsi",
    label="RSI",
    type="INDICATOR_NODE",
    tooltip="Measures momentum by calculating the ration of higher closes and lower closes after having been smoothed by an average, normalizing the result between 0 and 100.",
    docs_path="rsi.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp", label="Input",)],
    outputs=[Output()],
)


def rsi(inp, period):
    return btind.RSI(inp, period=period)


derivative_docs = Node(
    key="derivative",
    label="Derivative",
    type="INDICATOR_NODE",
    tooltip="Takes the derivative of line in respect to the period length.",
    docs_path="derivative.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI(default=1))],
    inputs=[Input(key="inp", label="Input",)],
    outputs=[Output()],
)


def derivative(inp, period):
    return inp(0) - inp(period)


momentum_docs = Module(
    key="momentum",
    label="Momentum",
    color=Color(red=0, green=200, blue=255),
    icon="fas fa-hippo",
    nodes=[
        commodity_channel_index_docs,
        rate_of_change_docs,
        rsi_docs,
        derivative_docs,
    ],
)

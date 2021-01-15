import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

rsi_docs = Node(
    key="rsi",
    label="RSI",
    type="INDICATOR_NODE",
    tooltip="Relative Strength Index - Measures momentum by calculating the ration of higher closes and lower closes after having been smoothed by an average, normalizing the result between 0 and 100.",
    docs_path="rsi.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input",)],
    outputs=[Output()],
)


def rsi(input0, period):
    return btind.RSI(input0, period=period, safediv=True)


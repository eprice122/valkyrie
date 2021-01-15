import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

triple_ema_docs = Node(
    key="triple_ema",
    label="Triple EMA",
    type="INDICATOR_NODE",
    tooltip="Moving average intended to reduce lag.",
    docs_path="",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output(label="Output")],
)


def triple_ema(input0, period):
    return btind.TripleExponentialMovingAverage(input0, period=period)

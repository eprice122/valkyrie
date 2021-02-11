import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

lookback_docs = Node(
    key="lookback",
    label="Lookback",
    type="INDICATOR_NODE",
    tooltip="Used to calculate previous tick data.",
    docs_path="lookback.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def lookback(input0, period):
    return input0(-period)

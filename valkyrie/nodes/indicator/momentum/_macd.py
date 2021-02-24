import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

macd_docs = Node(
    key="macd",
    label="MACD",
    type="INDICATOR_NODE",
    tooltip="Measures the distance of a short and a long term moving average to identify an emerging trend.",
    docs_path="macd.md",
    parameters=[
        Parameter(key="short_period", label="Short Period", ui=IntegerUI(default=12)),
        Parameter(key="long_period", label="Long Period", ui=IntegerUI(default=26)),
        Parameter(key="signal", label="Fast Period", ui=IntegerUI(default=9)),
    ],
    inputs=[Input(key="input0", label="Input")],
    outputs=[
        Output(key="macd", label="MACD"),
        Output(key="signal", label="Signal"),
        Output(key="histo", label="Difference"),
    ],
)


def macd(input0, short_period: int = 12, long_period: int = 26, signal: int = 9):
    return btind.MACDHisto(
        input0, period_me1=short_period, period_me2=long_period, period_signal=signal,
    )


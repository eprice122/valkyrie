import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

bollinger_bands_docs = Node(
    key="bollinger_bands",
    label="Bollinger Bands",
    type="INDICATOR_NODE",
    tooltip="Measures volatility by predicting an overbought (top band) and oversold (bottom band) market",
    docs_path="bollinger_bands.md",
    parameters=[
        Parameter(key="period", label="Period", ui=IntegerUI(default=30)),
        Parameter(key="devfactor", label="Dev Factor", ui=IntegerUI(default=2)),
    ],
    inputs=[Input(key="input0", label="Input")],
    outputs=[
        Output(label="Top", key="top"),
        Output(label="Middle", key="mid"),
        Output(label="Bottom", key="bot"),
    ],
)


def bollinger_bands(input0, period=20, devfactor=2):
    return btind.BollingerBands(input0, period=period, devfactor=devfactor)

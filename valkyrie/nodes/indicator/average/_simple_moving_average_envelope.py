import backtrader.indicators as btind

from ...entities import FloatUI, Input, IntegerUI, Node, Output, Parameter

sma_env_docs = Node(
    key="sma_env",
    label="Simple Moving Average Envelope",
    type="INDICATOR_NODE",
    tooltip="Non-weighted average of the last n periods. With top and bottom bands.",
    docs_path="simple_moving_average.md",
    parameters=[
        Parameter(key="period", label="Period", ui=IntegerUI()),
        Parameter(key="percent", label="Band Percent", ui=FloatUI(default=2.5)),
    ],
    inputs=[Input(key="inp")],
    outputs=[
        Output(label="SMA", key="sma"),
        Output(label="Top", key="top"),
        Output(label="Bottom", key="bot"),
    ],
)


def sma_env(inp, period, percent=2.5):
    return btind.SMAEnvelope(inp, period=period, perc=percent)

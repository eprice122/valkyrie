import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

average_true_range_docs = Node(
    key="average_true_range",
    label="Average True Range",
    type="INDICATOR_NODE",
    tooltip="Average volatility of the market during each tick.",
    docs_path="average_true_range.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[
        Input(key="high", label="High"),
        Input(key="low", label="Low"),
        Input(key="close", label="Close"),
    ],
    outputs=[Output(label="Output")],
)


def average_true_range(high, low, close, period):
    tr = true_range(high, low, close)
    return btind.MovingAverageSimple(tr, period=period)

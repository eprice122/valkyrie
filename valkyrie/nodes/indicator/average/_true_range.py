import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

true_range_docs = Node(
    key="true_range",
    label="True Range",
    type="INDICATOR_NODE",
    tooltip="Gauges the volatility of the market during each tick.",
    docs_path="true_range.md",
    parameters=[],
    inputs=[
        Input(key="high", label="High"),
        Input(key="low", label="Low"),
        Input(key="close", label="Close"),
    ],
    outputs=[Output(label="Output")],
)


def true_range(high, low, close):
    return btind.Max(abs(high - low), abs(high - close), abs(low - close))


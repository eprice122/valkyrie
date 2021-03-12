import backtrader.indicators as btind

from ...entities import FloatUI, Input, IntegerUI, Node, Output, Parameter

cci_docs = Node(
    key="cci",
    label="CCI",
    type="INDICATOR_NODE",
    tooltip="Measures variations of the “typical price” from its mean to identify extremes and reversals.",
    docs_path="commodity_channel_index.md",
    parameters=[
        Parameter(key="period", label="Period", ui=IntegerUI()),
        Parameter(key="factor", label="Factor", ui=FloatUI(default=0.015)),
    ],
    inputs=[],
    outputs=[Output()],
)


def cci(strategy, data, period: int, factor: float = 0.015):
    return btind.CommodityChannelIndex(data, period=period, factor=factor)

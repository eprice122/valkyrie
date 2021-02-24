import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

rank_docs = Node(
    key="rank",
    label="Percent Rank",
    type="INDICATOR_NODE",
    tooltip="Measures the percent rank of the current value with respect to that of period bars ago.",
    docs_path="rank.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def rank(input0, period):
    return btind.PercentRank()

import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter

sum_n_docs = Node(
    key="sum_n",
    label="Sum of Period",
    type="INDICATOR_NODE",
    tooltip="Calculates the sum of the data values over a given period.",
    docs_path="sum_n.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def sum_n(input0, period):
    return btind.SumN(input0, period=period)

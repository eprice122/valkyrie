import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter


class AllN(bt.Indicator):
    lines = ("If", "Else")

    def __init__(self, input0, period):
        self.lines.If = btind.AllN(input0, period=period)
        self.lines.Else = self.lines.If == False


all_n_docs = Node(
    key="all_n",
    label="All of Period",
    type="INDICATOR_NODE",
    tooltip="Outputs true if all of the values in the period evaluates to non-zero.",
    docs_path="all_n.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output(label="If", key="If"), Output(label="Else", key="Else")],
)


def all_n(input0, period):
    return AllN(input0=inp, period=period)

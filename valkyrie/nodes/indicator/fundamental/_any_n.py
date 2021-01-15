import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter


class AnyN(bt.Indicator):
    lines = ("If", "Else")

    def __init__(self, input0, period):
        self.lines.If = btind.AnyN(input0, period=period)
        self.lines.Else = self.lines.If == False


any_n_docs = Node(
    key="any_n",
    label="Any in Period",
    type="INDICATOR_NODE",
    tooltip="Has a value of True (stored as 1.0 in the lines) if any of the values in the period evaluates to non-zero.",
    docs_path="any_n.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def any_n(input0, period):
    return AnyN(input0=input0, period=period)

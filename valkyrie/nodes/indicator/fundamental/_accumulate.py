import backtrader as bt

from ...entities import FloatUI, Input, Node, Output, Parameter


class Accumulate(bt.Indicator):
    # https://www.backtrader.com/blog/posts/2018-01-27-recursive-indicators/recursive-indicator/
    lines = ("accumulate",)

    def __init__(self):
        pass

    def nextstart(self):
        self.lines.accumulate[0] = 0

    def next(self):
        self.lines.accumulate[0] = self.lines.accumulate[-1] + self.data[0]


accumulate_docs = Node(
    key="accumulate",
    label="Accumulate",
    type="INDICATOR_NODE",
    tooltip="Total sum of all previous values.",
    docs_path="accumulate.md",
    parameters=[],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)


def accumulate(input0):
    return Accumulate(input0).accumulate

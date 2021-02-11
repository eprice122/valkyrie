import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, Node, Output


class OrLogic(bt.Indicator):
    lines = ("If", "Else")

    def __init__(self, inputs):
        for i, inp in enumerate(inputs):
            if i == 0:
                combo = inp
            else:
                combo = btind.Or(combo, inp)
        self.lines.If = combo
        self.lines.Else = combo == False


or_logic_docs = Node(
    key="or_logic",
    label="Or",
    type="INDICATOR_NODE",
    tooltip="",
    docs_path="or_logic.md",
    parameters=[],
    inputs=[Input(key="inputs", label="Inputs", multi=True)],
    outputs=[Output(label="If", key="If"), Output(label="Else", key="Else")],
)


def or_logic(inputs):
    return OrLogic(inputs=inputs)

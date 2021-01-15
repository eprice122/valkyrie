import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, Node, Output


class AndLogic(bt.Indicator):
    lines = ("If", "Else")

    def __init__(self, inputs):
        for i, inp in enumerate(inputs):
            if i == 0:
                combo = inp
            else:
                combo = btind.And(combo, inp)
        self.lines.If = combo
        self.lines.Else = combo == False


and_logic_docs = Node(
    key="and_logic",
    label="And",
    type="INDICATOR_NODE",
    tooltip="",
    docs_path="",
    parameters=[],
    inputs=[Input(key="inputs", label="Inputs", multi=True)],
    outputs=[Output(label="If", key="If"), Output(label="Else", key="Else")],
)


def and_logic(inputs):
    return AndLogic(inputs=inputs)

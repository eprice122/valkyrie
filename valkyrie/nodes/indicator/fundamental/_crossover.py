import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, Node, Output, Parameter, SelectorUI

GREATER_THAN = 0
GREATER_EQUAL = 1
LESS_THAN = 2
LESS_EQUAL = 3
EQUAL = 4
NOT_EQUAL = 5


class Crossover(bt.Indicator):
    lines = ("If", "Else")

    def __init__(self, input0, input1, logic):
        if logic == GREATER_THAN:
            result = input0 > input1
        elif logic == GREATER_EQUAL:
            result = input0 >= input1
        elif logic == LESS_THAN:
            result = input0 < input1
        elif logic == LESS_EQUAL:
            result = input0 <= input1
        elif logic == EQUAL:
            result = input0 == input1
        elif logic == NOT_EQUAL:
            result = input0 != input1
        else:
            raise ValueError
        self.lines.If = result
        self.lines.Else = result == False


crossover_docs = Node(
    key="crossover",
    label="Crossover",
    type="INDICATOR_NODE",
    tooltip="Compares two nodes with the specified crossover operation.",
    docs_path="crossover.md",
    parameters=[
        Parameter(
            key="logic",
            label="Crossover Type",
            ui=SelectorUI(
                options={
                    "Greater Than": GREATER_THAN,
                    "Greater Equal": GREATER_EQUAL,
                    "Less Than": LESS_THAN,
                    "Less Equal": LESS_EQUAL,
                    "Equal": EQUAL,
                    "Not Equal": NOT_EQUAL,
                }
            ),
        )
    ],
    inputs=[Input(key="input0", label="Input 1"), Input(key="input1", label="Input 2")],
    outputs=[Output(label="If", key="If"), Output(label="Else", key="Else")],
)


def crossover(input0, input1, logic):
    return Crossover(input0=input0, input1=input1, logic=logic)


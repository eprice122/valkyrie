import backtrader as bt

from ...entities import FloatUI, Input, IntegerUI, Node, Output, Parameter, SelectorUI
from ._crossover import (
    EQUAL,
    GREATER_EQUAL,
    GREATER_THAN,
    LESS_EQUAL,
    LESS_THAN,
    Crossover,
)

constant_crossover_docs = Node(
    key="constant_crossover",
    label="Constant Crossover",
    type="INDICATOR_NODE",
    tooltip="Compares a node with a constant value using the specified crossover.",
    docs_path="constant_crossover.md",
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
                }
            ),
        ),
        Parameter(key="value", label="Value", ui=FloatUI()),
    ],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="If", key="If"), Output(label="Else", key="Else")],
)


def constant_crossover(input0, logic, value):
    return Crossover(input0=input0, input1=value, logic=logic)

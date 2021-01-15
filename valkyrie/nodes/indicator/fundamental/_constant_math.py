from ...entities import FloatUI, Input, Node, Output, Parameter, SelectorUI
from ._math import (
    ADDITION,
    DIVISION,
    EXPONENTIAL,
    MULTIPLICATION,
    SUBTRACTION,
    arithmetic,
)

constant_math_docs = Node(
    key="constant_math",
    label="Constant Math",
    type="INDICATOR_NODE",
    tooltip="Arithmetic operations (+ - * /) between a node and a constant value.",
    docs_path="constant_math.md",
    parameters=[
        Parameter(
            key="logic",
            label="Logic",
            ui=SelectorUI(
                options={
                    "Addition": ADDITION,
                    "Subtraction": SUBTRACTION,
                    "Multiplication": MULTIPLICATION,
                    "Division": DIVISION,
                    "Exponential": EXPONENTIAL,
                }
            ),
        ),
        Parameter(key="value", label="Value", ui=FloatUI()),
    ],
    inputs=[Input(key="input0", label="Input 1"),],
    outputs=[Output()],
)


def constant_math(input0, value, logic):
    return arithmetic(input0, value, logic)

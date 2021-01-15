from ...entities import FloatUI, Input, Node, Output, Parameter, SelectorUI

ADDITION = 0
SUBTRACTION = 1
MULTIPLICATION = 2
DIVISION = 3
EXPONENTIAL = 4


def arithmetic(input0, input1, logic):
    if logic == ADDITION:
        return input0 + input1
    elif logic == SUBTRACTION:
        return input0 - input1
    elif logic == MULTIPLICATION:
        return input0 * input1
    elif logic == DIVISION:
        return input0 / input1
    elif logic == EXPONENTIAL:
        return input0 ** input1
    else:
        raise ValueError


math_docs = Node(
    key="math",
    label="Math",
    type="INDICATOR_NODE",
    tooltip="Arithmetic operations (+ - * /) between two nodes.",
    docs_path="math.md",
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
        )
    ],
    inputs=[Input(key="input0", label="Input 1"), Input(key="input1", label="Input 2")],
    outputs=[Output()],
)


def math(input0, input1, logic):
    return arithmetic(input0, input1, logic)

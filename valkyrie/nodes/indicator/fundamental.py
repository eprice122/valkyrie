import backtrader.indicators as btind

from ..entities import (
    Color,
    Input,
    IntegerUI,
    Module,
    Node,
    Output,
    Parameter,
    SelectorUI,
)

GREATER_THAN = 0
GREATER_EQUAL = 1
LESS_THAN = 2
LESS_EQUAL = 3
EQUAL = 4
NOT_EQUAL = 5

comparator_docs = Node(
    key="comparator",
    label="Comparator",
    type="INDICATOR_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="logic",
            label="Logic",
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
    outputs=[Output(label="Output")],
)


def comparator(input0, input1, logic):
    if logic == GREATER_THAN:
        return input0 > input1
    elif logic == GREATER_EQUAL:
        return input0 >= input1
    elif logic == LESS_THAN:
        return input0 < input1
    elif logic == LESS_EQUAL:
        return input0 <= input1
    elif logic == EQUAL:
        return input0 == input1
    elif logic == NOT_EQUAL:
        return input0 != input1
    else:
        raise ValueError


ADDITION = 0
SUBTRACTION = 1
MULTIPLICATION = 2
DIVISION = 3
EXPONENTIAL = 4

arithmetic_docs = Node(
    key="arithmetic",
    label="Arithmetic",
    type="INDICATOR_NODE",
    tooltip="",
    docs_path="",
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
    outputs=[Output(label="Output")],
)


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


bollinger_bands_docs = Node(
    key="bollinger_bands",
    label="Bollinger Bands",
    type="INDICATOR_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(key="period", label="Period", ui=IntegerUI()),
        Parameter(key="devfactor", label="Dev Factor", ui=IntegerUI()),
    ],
    inputs=[Input(key="inp", label="Input")],
    outputs=[
        Output(label="Top", key="top"),
        Output(label="Middle", key="mid"),
        Output(label="Bottom", key="bot"),
    ],
)


def bollinger_bands(inp, period=20, devfactor=2):
    return btind.BollingerBands(inp, period=period, devfactor=devfactor)


fundamental_docs = Module(
    key="fundamental",
    label="Fundamental",
    color=Color(red=249, green=168, blue=37),
    icon="fas fa-square-root-alt",
    nodes=[comparator_docs, arithmetic_docs, bollinger_bands_docs],
)

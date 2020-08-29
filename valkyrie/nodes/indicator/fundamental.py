import backtrader.indicators as btind

from ..entities import (
    Color,
    FloatUI,
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

node_comparator_docs = Node(
    key="node_comparator",
    label="Node Comparator",
    type="INDICATOR_NODE",
    tooltip="Compares two nodes with the specified comparator.",
    docs_path="node_comparator.md",
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


def node_comparator(input0, input1, logic):
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


constant_comparator_docs = Node(
    key="constant_comparator",
    label="Constant Comparator",
    type="INDICATOR_NODE",
    tooltip="Compares a node with a constant value using the specified comparator.",
    docs_path="constant_comparator.md",
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
        ),
        Parameter(key="value", label="Value", ui=FloatUI()),
    ],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="Output")],
)


def constant_comparator(inp, value, logic):
    if logic == GREATER_THAN:
        return inp > value
    elif logic == GREATER_EQUAL:
        return inp >= value
    elif logic == LESS_THAN:
        return inp < value
    elif logic == LESS_EQUAL:
        return inp <= value
    elif logic == EQUAL:
        return inp == value
    elif logic == NOT_EQUAL:
        return inp != value
    else:
        raise ValueError


AND = 0
OR = 1

logic_docs = Node(
    key="logic",
    label="Logic",
    type="INDICATOR_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="logic", label="Logic", ui=SelectorUI(options={"And": AND, "Or": OR}),
        )
    ],
    inputs=[Input(key="inputs", label="Inputs", multi=True)],
    outputs=[Output(label="Output")],
)


def logic(inputs, logic):
    for i, inp in enumerate(inputs):
        if i == 0:
            combo = inp
        else:
            if logic == AND:
                combo = btind.And(combo, inp)
            elif logic == OR:
                combo = btind.Or(combo, inp)
            else:
                raise ValueError
    return combo


ADDITION = 0
SUBTRACTION = 1
MULTIPLICATION = 2
DIVISION = 3
EXPONENTIAL = 4

node_arithmetic_docs = Node(
    key="node_arithmetic",
    label="Node Arithmetic",
    type="INDICATOR_NODE",
    tooltip="Arithmetic operations (+ - * /) between two nodes.",
    docs_path="node_arithmetic.md",
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


def node_arithmetic(input0, input1, logic):
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


constant_arithmetic_docs = Node(
    key="constant_arithmetic",
    label="Constant Arithmetic",
    type="INDICATOR_NODE",
    tooltip="Arithmetic operations (+ - * /) between a node and a constant value.",
    docs_path="constant_arithmetic.md",
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
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="Output")],
)


def constant_arithmetic(inp, value, logic):
    if logic == ADDITION:
        return inp + value
    elif logic == SUBTRACTION:
        return inp - value
    elif logic == MULTIPLICATION:
        return inp * value
    elif logic == DIVISION:
        return inp / value
    elif logic == EXPONENTIAL:
        return inp ** value
    else:
        raise ValueError


rank_docs = Node(
    key="percent_rank",
    label="Percent Rank",
    type="INDICATOR_NODE",
    tooltip="Measures the percent rank of the current value with respect to that of period bars ago",
    docs_path="rank.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="Output")],
)


def percent_rank(inp, period):
    return btind.PercentRank()


all_n_docs = Node(
    key="all_n",
    label="All Previous",
    type="INDICATOR_NODE",
    tooltip="Has a value of True (stored as 1.0 in the lines) if all of the values in the period evaluates to non-zero.",
    docs_path="all_n.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="Output")],
)


def all_n(inp, period):
    return btind.AllN(inp, period=period)


any_n_docs = Node(
    key="any_n",
    label="Any Previous",
    type="INDICATOR_NODE",
    tooltip="Has a value of True (stored as 1.0 in the lines) if any of the values in the period evaluates to non-zero.",
    docs_path="any_n.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="Output")],
)


def any_n(inp, period):
    return btind.AllN(inp, period=period)


sum_n_docs = Node(
    key="sum_n",
    label="Sum of Previous",
    type="INDICATOR_NODE",
    tooltip="Calculates the Sum of the data values over a given period.",
    docs_path="sum_n.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="inp", label="Input")],
    outputs=[Output(label="Output")],
)


def sum_n(inp, period):
    return btind.SumN(inp, period=period)


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


fundamental_module = Module(
    key="fundamental",
    label="Fundamental",
    color=Color(red=249, green=168, blue=37),
    icon="fas fa-square-root-alt",
    nodes=[
        node_comparator_docs,
        constant_comparator_docs,
        node_arithmetic_docs,
        constant_arithmetic_docs,
        logic_docs,
        all_n_docs,
        any_n_docs,
        sum_n_docs,
        bollinger_bands_docs,
    ],
)

import backtrader as bt

from ...entities import FloatUI, Node, Output, Parameter

constant_docs = Node(
    key="constant",
    label="Constant Value",
    type="INDICATOR_NODE",
    tooltip="Constant number. Useful for comparisons and math.",
    docs_path="constant.md",
    parameters=[Parameter(key="value", label="Value", ui=FloatUI())],
    inputs=[],
    outputs=[Output(label="Value")],
)


def constant(data, value):
    return bt.If(True, value, None)

import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, Node, Output

switch_docs = Node(
    key="switch",
    label="Switch",
    type="INDICATOR_NODE",
    tooltip="Outputs the input or null based on the input switch state provided.",
    docs_path="switch.md",
    parameters=[],
    inputs=[Input(key="input0"), Input(key="state", label="State")],
    outputs=[Output()],
)


def switch(input0, state):
    return bt.If(state > 0, input0, 0)

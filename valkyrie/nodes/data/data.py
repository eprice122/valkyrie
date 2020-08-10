import backtrader.indicators as btind

from ..entities import Color, Input, Module, Node, Output, Parameter, SelectorUI

market_docs = Node(
    key="market",
    label="Equities",
    type="MARKET_NODE",
    tooltip="",
    docs_path="",
    parameters=[],
    inputs=[],
    outputs=[
        Output(key="open", label="Open"),
        Output(key="high", label="High"),
        Output(key="low", label="Low"),
        Output(key="close", label="Close"),
        Output(key="volume", label="Volume"),
    ],
)


data_docs = Module(
    key="market",
    label="Market",
    color=Color(red=170, green=0, blue=255),
    icon="fas fa-chart-line",
    nodes=[market_docs],
)

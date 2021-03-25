import backtrader as bt
import backtrader.indicators as btind

from ...entities import Input, IntegerUI, Node, Output, Parameter


class RateOfChange(bt.Indicator):
    lines = ("roc",)

    def __init__(self, input0, period):
        dperiod = input0(-period)
        self.lines.roc = btind.DivByZero((input0 - dperiod), dperiod)


rate_of_change_docs = Node(
    key="rate_of_change",
    label="Rate of Change",
    type="INDICATOR_NODE",
    tooltip="Measures the ratio of change in prices over a period.",
    docs_path="rate_of_change.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0", label="Input")],
    outputs=[Output()],
)


def rate_of_change(input0, period):
    return RateOfChange(input0=input0, period=period).roc


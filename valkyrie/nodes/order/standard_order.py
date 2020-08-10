from datetime import datetime, timedelta

from backtrader import Order, Strategy

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

market_order_docs = Node(
    key="market_order",
    label="Market Order",
    type="ORDER_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(key="price", label="Price", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def market_order(
    self: Strategy, data, inp, side: str, size: int, price: float = None,
):
    price = self.data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        self.buy(
            data=data, size=size, price=price, exectype=Order.Market,
        )
    elif side == "SELL" and inp[0] == 1:
        self.sell(
            data=data, size=size, price=price, exectype=Order.Market,
        )


stop_order_docs = Node(
    key="stop_order",
    label="Stop Order",
    type="ORDER_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(key="price", label="Stop Price", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def stop_order(
    self: Strategy, data, inp, side: str, size: int, price: float,
):
    price = self.data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        self.buy(
            data=data, size=size, price=price, exectype=Order.Stop,
        )
    elif side == "SELL" and inp[0] == 1:
        self.sell(
            data=data, size=size, price=price, exectype=Order.Stop,
        )


limit_order_docs = Node(
    key="limit_order",
    label="Limit Order",
    type="ORDER_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(key="price", label="Limit Price", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def limit_order(
    self: Strategy, data, inp, side: str, size: int, price: float,
):
    price = self.data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        self.buy(
            data=data, size=size, price=price, exectype=Order.Limit,
        )
    elif side == "SELL" and inp[0] == 1:
        self.sell(
            data=data, size=size, price=price, exectype=Order.Limit,
        )


stop_limit_order_docs = Node(
    key="stop_limit_order",
    label="Stop Limit Order",
    type="ORDER_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(key="price", label="Stop Price", ui=FloatUI()),
        Parameter(key="plimit", label="Limit Price", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def stop_limit_order(
    self: Strategy, data, inp, side: str, size: int, price: float, plimit: float,
):
    price = self.data.close[0] * price
    plimit = self.data.close[0] * plimit
    if side == "BUY" and inp[0] == 1:
        self.buy(
            data=data, size=size, price=price, plimit=plimit, exectype=Order.StopLimit,
        )
    elif side == "SELL" and inp[0] == 1:
        self.sell(
            data=data, size=size, price=price, plimit=plimit, exectype=Order.StopLimit,
        )


stop_trail_docs = Node(
    key="stop_trail",
    label="Stop Trail Order",
    type="ORDER_NODE",
    tooltip="",
    docs_path="",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(key="price", label="Trigger Price", ui=FloatUI()),
        Parameter(key="trail_percent", label="Trail Percent", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[Output()],
)


def stop_trail(
    self: Strategy, data, inp, side: str, size: int, price: float, trail_percent: float,
):
    price = self.data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        self.buy(
            data=data,
            size=size,
            price=price,
            trail_percent=trail_percent,
            exectype=Order.StopTrail,
        )
    elif side == "SELL" and inp[0] == 1:
        self.sell(
            data=data,
            size=size,
            price=price,
            trail_percent=trail_percent,
            exectype=Order.StopTrail,
        )


basic_order_docs = Module(
    key="basic_order",
    label="Orders",
    color=Color(red=2, green=78, blue=101),
    icon="fas fa-balance-scale-left",
    nodes=[
        market_order_docs,
        stop_order_docs,
        limit_order_docs,
        stop_limit_order_docs,
        stop_trail_docs,
    ],
)

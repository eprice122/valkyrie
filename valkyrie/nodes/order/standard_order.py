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
    tooltip="Executes order at the opening of the next tick.",
    docs_path="market_order.md",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def market_order(
    strategy: Strategy, data, inp, side: str, size: int,
):
    if data.symbol == "A":
        x = inp[0]
        y = 0

    if side == "BUY" and inp[0] == 1:
        strategy.buy(
            data=data, size=size, exectype=Order.Market,
        )
    elif side == "SELL" and inp[0] == 1:
        strategy.sell(
            data=data, size=size, exectype=Order.Market,
        )


stop_order_docs = Node(
    key="stop_order",
    label="Stop Order",
    type="ORDER_NODE",
    tooltip="Triggers a market order when the price crosses specified value.",
    docs_path="stop_order.md",
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
    outputs=[],
)


def stop_order(
    strategy: Strategy, data, inp, side: str, size: int, price: float,
):
    price = data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        strategy.buy(
            data=data, size=size, price=price, exectype=Order.Stop,
        )
    elif side == "SELL" and inp[0] == 1:
        strategy.sell(
            data=data, size=size, price=price, exectype=Order.Stop,
        )


limit_order_docs = Node(
    key="limit_order",
    label="Limit Order",
    type="ORDER_NODE",
    tooltip="Executes a market order when the input crosses the specified price.",
    docs_path="limit_order.md",
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
    outputs=[],
)


def limit_order(
    strategy: Strategy, data, inp, side: str, size: int, price: float,
):
    price = data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        strategy.buy(
            data=data, size=size, price=price, exectype=Order.Limit,
        )
    elif side == "SELL" and inp[0] == 1:
        strategy.sell(
            data=data, size=size, price=price, exectype=Order.Limit,
        )


stop_limit_order_docs = Node(
    key="stop_limit_order",
    label="Stop Limit Order",
    type="ORDER_NODE",
    tooltip="Executes a limit order when the input crosses the specified price.",
    docs_path="stop_limit_order.md",
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
    outputs=[],
)


def stop_limit_order(
    strategy: Strategy, data, inp, side: str, size: int, price: float, plimit: float,
):
    price = data.close[0] * price
    plimit = data.close[0] * plimit
    if side == "BUY" and inp[0] == 1:
        strategy.buy(
            data=data, size=size, price=price, plimit=plimit, exectype=Order.StopLimit,
        )
    elif side == "SELL" and inp[0] == 1:
        strategy.sell(
            data=data, size=size, price=price, plimit=plimit, exectype=Order.StopLimit,
        )


stop_trail_docs = Node(
    key="stop_trail",
    label="Stop Trail Order",
    type="ORDER_NODE",
    tooltip="Follows trend and triggers a market order when the trend is reversed by a specified amount.",
    docs_path="stop_trail_order.md",
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
    outputs=[],
)


def stop_trail(
    strategy: Strategy,
    data,
    inp,
    side: str,
    size: int,
    price: float,
    trail_percent: float,
):
    price = data.close[0] * price
    if side == "BUY" and inp[0] == 1:
        strategy.buy(
            data=data,
            size=size,
            price=price,
            trail_percent=trail_percent,
            exectype=Order.StopTrail,
        )
    elif side == "SELL" and inp[0] == 1:
        strategy.sell(
            data=data,
            size=size,
            price=price,
            trail_percent=trail_percent,
            exectype=Order.StopTrail,
        )


basic_order_docs = Module(
    key="standard_order",
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

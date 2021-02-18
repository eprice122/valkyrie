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

LIMIT_ORDER = 0
STOP_ORDER = 1
STOPTRAIL_ORDER = 2
MARKET_ORDER = 3


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
        Parameter(key="trigger_percent", label="Stop Percent", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def stop_order(
    strategy: Strategy, data, inp, side: str, size: int, trigger_percent: float,
):
    price = _set_trigger_price(trigger_percent, data.close[0])
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
        Parameter(key="trigger_percent", label="Limit Percent", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def limit_order(
    strategy: Strategy, data, inp, side: str, size: int, trigger_percent: float,
):
    price = _set_trigger_price(trigger_percent, data.close[0])
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
        Parameter(key="trigger_percent", label="Stop Percent", ui=FloatUI()),
        Parameter(key="limit_percent", label="Limit Percent", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def stop_limit_order(
    strategy: Strategy,
    data,
    inp,
    side: str,
    size: int,
    trigger_percent: float,
    limit_percent: float,
):
    price = _set_trigger_price(trigger_percent, data.close[0])
    plimit = _set_trigger_price(limit_percent, data.close[0])
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
        Parameter(key="trail_percent", label="Trail Percent", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def stop_trail(
    strategy: Strategy, data, inp, side: str, size: int, trail_percent: float,
):
    trail_percent = _set_stop_trail_trigger(trail_percent)
    if side == "BUY" and inp[0] == 1:
        strategy.buy(
            data=data, size=size, trailpercent=trail_percent, exectype=Order.StopTrail,
        )
    elif side == "SELL" and inp[0] == 1:
        strategy.sell(
            data=data, size=size, trailpercent=trail_percent, exectype=Order.StopTrail,
        )


market_bracket_order_docs = Node(
    key="market_bracket_order",
    label="Market Bracket Order",
    type="ORDER_NODE",
    tooltip="An entrance market order, low order, and a high order issued simultaneously to secure profits/risk in between.",
    docs_path="market_bracket_order.md",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(
            key="upper_type",
            label="Upper Type",
            ui=SelectorUI(
                options={
                    "Limit Order": LIMIT_ORDER,
                    "Stop Order": STOP_ORDER,
                    "Stop Trail Order": STOPTRAIL_ORDER,
                }
            ),
        ),
        Parameter(key="upper_trigger", label="Upper Trigger", ui=FloatUI()),
        Parameter(
            key="lower_type",
            label="Lower Type",
            ui=SelectorUI(
                options={
                    "Limit Order": LIMIT_ORDER,
                    "Stop Order": STOP_ORDER,
                    "Stop Trail Order": STOPTRAIL_ORDER,
                }
            ),
        ),
        Parameter(key="lower_trigger", label="Lower Trigger", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def market_bracket_order(
    strategy: Strategy,
    data,
    inp,
    side,
    size,
    upper_type,
    upper_trigger,
    lower_type,
    lower_trigger,
):
    kwargs = _set_kwargs(
        data=data,
        middle_type=MARKET_ORDER,
        upper_type=upper_type,
        upper_trigger=upper_trigger,
        lower_type=lower_type,
        lower_trigger=lower_trigger,
    )
    if side == "BUY" and inp[0] == 1:
        strategy.buy_bracket(data=data, size=size, **kwargs)
    elif side == "SELL" and inp[0] == 1:
        strategy.sell_bracket(data=data, size=size, **kwargs)


limit_bracket_order_docs = Node(
    key="limit_bracket_order",
    label="Limit Bracket Order",
    type="ORDER_NODE",
    tooltip="An entrance limit order, low order, and a high order issued simultaneously to secure profits/risk in between.",
    docs_path="limit_bracket_order.md",
    parameters=[
        Parameter(
            key="side",
            label="Side",
            ui=SelectorUI(options={"Buy": "BUY", "Sell": "SELL"}),
        ),
        Parameter(key="size", label="Size", ui=IntegerUI()),
        Parameter(key="middle_trigger", label="Limit Price", ui=FloatUI()),
        Parameter(
            key="upper_type",
            label="Upper Type",
            ui=SelectorUI(
                options={
                    "Limit Order": LIMIT_ORDER,
                    "Stop Order": STOP_ORDER,
                    "Stop Trail Order": STOPTRAIL_ORDER,
                }
            ),
        ),
        Parameter(key="upper_trigger", label="Upper Trigger", ui=FloatUI()),
        Parameter(
            key="lower_type",
            label="Lower Type",
            ui=SelectorUI(
                options={
                    "Limit Order": LIMIT_ORDER,
                    "Stop Order": STOP_ORDER,
                    "Stop Trail Order": STOPTRAIL_ORDER,
                }
            ),
        ),
        Parameter(key="lower_trigger", label="Lower Trigger", ui=FloatUI()),
    ],
    inputs=[Input(key="inp")],
    outputs=[],
)


def limit_bracket_order(
    strategy: Strategy,
    data,
    inp,
    side,
    size,
    upper_type,
    upper_trigger,
    middle_trigger,
    lower_type,
    lower_trigger,
):
    kwargs = _set_kwargs(
        data=data,
        middle_type=LIMIT_ORDER,
        middle_trigger=middle_trigger,
        upper_type=upper_type,
        upper_trigger=upper_trigger,
        lower_type=lower_type,
        lower_trigger=lower_trigger,
    )
    if side == "BUY" and inp[0] == 1:
        strategy.buy_bracket(data=data, size=size, **kwargs)
    elif side == "SELL" and inp[0] == 1:
        strategy.sell_bracket(data=data, size=size, **kwargs)


basic_order_docs = Module(
    key="standard_order",
    label="Orders",
    color=Color(red=250, green=127, blue=25),
    icon="fas fa-balance-scale-left",
    nodes=[
        market_order_docs,
        stop_order_docs,
        limit_order_docs,
        stop_limit_order_docs,
        stop_trail_docs,
        limit_bracket_order_docs,
        market_bracket_order_docs,
    ],
)


def _set_kwargs(
    data,
    middle_type,
    upper_type,
    upper_trigger,
    lower_type,
    lower_trigger,
    middle_trigger=None,
):
    kwargs = {}

    if middle_type == MARKET_ORDER:
        kwargs["exectype"] = Order.Market
    if middle_type == LIMIT_ORDER:
        kwargs["exectype"] = Order.Limit
        kwargs["oargs"] = {
            "limitprice": _set_trigger_price(middle_trigger, data.close[0])
        }

    if upper_type == LIMIT_ORDER:
        kwargs["limitexec"] = Order.Limit
        kwargs["limitargs"] = {
            "limitprice": _set_trigger_price(upper_trigger, data.close[0])
        }
    elif upper_type == STOP_ORDER:
        kwargs["limitexec"] = Order.Stop
        kwargs["limitargs"] = {
            "stopprice": _set_trigger_price(upper_trigger, data.close[0])
        }
    elif upper_type == STOPTRAIL_ORDER:
        kwargs["stopexec"] = Order.StopTrail
        kwargs["stopargs"] = {"trailpercent": _set_stop_trail_trigger(upper_trigger)}
    else:
        raise ValueError

    if lower_type == STOP_ORDER:
        kwargs["stopexec"] = Order.Stop
        kwargs["stopargs"] = {
            "stopprice": _set_trigger_price(lower_trigger, data.close[0])
        }
    elif lower_type == LIMIT_ORDER:
        kwargs["stopexec"] = Order.Limit
        kwargs["stopargs"] = {
            "limitprice": _set_trigger_price(lower_trigger, data.close[0])
        }
    elif lower_type == STOPTRAIL_ORDER:
        kwargs["stopexec"] = Order.StopTrail
        kwargs["stopargs"] = {"trailpercent": _set_stop_trail_trigger(lower_trigger)}
    else:
        raise ValueError

    return kwargs


def _set_trigger_price(trigger_percent: float, close: float):
    trigger_percent += 100  # + 100%
    trigger_percent /= 100  # turned into a float
    return close * trigger_percent


def _set_stop_trail_trigger(trail_percent: float):
    return trail_percent / 100

import importlib
from typing import Callable, Dict

from backtrader import Cerebro
from backtrader.linebuffer import LineBuffer


def build_indicator(strategy, data, constructor: dict, nodes: dict):
    kwargs = constructor["parameters"]
    for key, props in constructor["inputs"].items():
        if not props["multi"]:
            value = props["value"][0]
            if value["port_id"] != "null":
                kwargs[key] = getattr(nodes[value["node_id"]], value["port_id"])
            else:
                kwargs[key] = nodes[value["node_id"]]
        else:
            kwargs[key] = set()
            for value in props["value"]:
                if value["port_id"] != "null":
                    kwargs[key].add(getattr(nodes[value["node_id"]], value["port_id"]))
                else:
                    kwargs[key].add(nodes[value["node_id"]])

    if len(constructor["inputs"].items()) == 0:
        kwargs["data"] = data
        kwargs["strategy"] = strategy

    indicator = parse_indicator(
        module_str=constructor["module_str"], node_str=constructor["node_str"]
    )(**kwargs)
    return indicator


def build_order(strategy, constructor, nodes):
    indicator = parse_order(
        module_str=constructor["module_str"], node_str=constructor["node_str"]
    )
    kwargs = constructor["parameters"]
    for key, props in constructor["inputs"].items():
        value = props["value"][0]
        if value["port_id"] != "null":
            kwargs[key] = getattr(nodes[value["node_id"]], value["port_id"])
        else:
            kwargs[key] = nodes[value["node_id"]]

    def func(data):
        return indicator(strategy=strategy, data=data, **kwargs)

    return func


def parse_indicator(module_str: str, node_str: str) -> Callable:
    return _parse(f"indicator.{module_str}", node_str)


def parse_order(module_str: str, node_str: str) -> Callable:
    return _parse(f"order.{module_str}", node_str)


def _parse(module_str, node_str):
    module = importlib.import_module(f".nodes.{module_str}", package="valkyrie")
    indicator = getattr(module, node_str)
    return indicator


def get_market(cerebro: Cerebro) -> Dict[str, dict]:
    market = dict()
    for symbol, datas in cerebro.datasbyname.items():
        market[symbol] = {
            "open": list(datas.lines.open.array),
            "high": list(datas.lines.high.array),
            "low": list(datas.lines.low.array),
            "close": list(datas.lines.close.array),
            "volume": list(datas.lines.volume.array),
        }
    return market

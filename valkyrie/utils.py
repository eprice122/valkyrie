import importlib
from typing import Callable


def build_indicator(constructor: dict, nodes: dict):
    kwargs = constructor["parameters"]
    for key, props in constructor["inputs"].items():
        if not props["multi"]:
            value = props["value"][0]
            if value["port_id"] != "null":
                kwargs[key] = getattr(nodes[value["node_id"]], value["port_id"])
            else:
                kwargs[key] = nodes[value["node_id"]]

    indicator = parse_indicator(
        module_str=constructor["module_str"], node_str=constructor["node_str"]
    )(**kwargs)
    return indicator


def build_beacon(self, constructor, nodes):
    indicator = parse_beacon(
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
        return indicator(self=self, data=data, **kwargs)

    return func


def parse_indicator(module_str: str, node_str: str) -> Callable:
    return _parse(f"indicator.{module_str}", node_str)


def parse_beacon(module_str: str, node_str: str) -> Callable:
    return _parse(f"order.{module_str}", node_str)


def _parse(module_str, node_str):
    module = importlib.import_module(f".nodes.{module_str}", package="valkyrie")
    indicator = getattr(module, node_str)
    return indicator

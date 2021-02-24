import os
from datetime import datetime
from typing import List
from uuid import uuid4

from backtrader import TimeFrame
from valkyrie.api import api
from valkyrie.configs import BrokerConfig, MarketConfig


def use_api(
    graph: List[dict],
    task_id: str = str(uuid4()),
    broker_config: BrokerConfig = BrokerConfig(cash=100_000_000),
    market_config: MarketConfig = MarketConfig(
        from_date=datetime(year=2014, month=1, day=1),
        to_date=datetime(year=2014, month=1, day=4),
        timeframe=TimeFrame.Minutes,
        symbols=["A", "F"],
    ),
    env: dict = {"unittest": True},
):
    return api(
        graph=graph,
        task_id=task_id,
        broker_config=broker_config,
        market_config=market_config,
        env=env,
    )


def use_market_node(id: str):
    return {
        "node_str": "market",
        "module_str": "market",
        "id": id,
        "type": "MARKET_NODE",
        "parameters": {},
        "inputs": {},
        "outputs": ["open", "high", "low", "close", "volume"],
    }

from datetime import datetime
from typing import Set

from backtrader import TimeFrame


class BrokerConfig:
    def __init__(self, cash: float):
        self.cash = cash


class MarketConfig:
    def __init__(
        self, from_date: datetime, to_date: datetime, timeframe: TimeFrame, symbols: Set[str],
    ):
        self.from_date = from_date
        self.to_date = to_date
        self.timeframe = timeframe
        self.symbols = symbols

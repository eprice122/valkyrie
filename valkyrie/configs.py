import logging
import sys
from datetime import datetime
from typing import Set

from backtrader import TimeFrame

from .feeds.virtual import VirtualFeed

# Create logger
logger = logging.getLogger(__name__)


class BrokerConfig:
    def __init__(self, cash: float):
        self.cash = cash


class MarketConfig:
    def __init__(
        self,
        from_date: datetime,
        to_date: datetime,
        timeframe: TimeFrame,
        symbols: Set[str],
    ):
        self.from_date = from_date
        self.to_date = to_date
        self.timeframe = timeframe
        self.symbols = symbols


def configure_market(cerebro, market_config, interupt_handler):
    logger.info("Adding feeds to cerebro")
    for symbol in market_config.symbols:
        feed: VirtualFeed = VirtualFeed(
            symbol=symbol,
            fromdate=market_config.from_date,
            todate=market_config.to_date,
            timeframe=market_config.timeframe,
            interupt_handler=interupt_handler,
        )  # type: ignore
        try:
            feed.virtual_load()
        except StopIteration:
            continue
        cerebro.adddata(feed, name=symbol)


def configure_broker(cerebro, broker_config):
    logger.info("Configuring Broker")
    cerebro.broker.setcash(broker_config.cash)

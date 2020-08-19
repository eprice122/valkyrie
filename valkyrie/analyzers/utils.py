import logging
import sys
from collections import OrderedDict

import backtrader.analyzers as btanalyzers
import pandas as pd
import quantstats as qs
import simplejson

from ..feeds.utils import get_benchmark
from .cash_market import CashMarket

# Create logger
logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def add_analyzers(cerebro):
    logger.info("Adding analyzers to cerebro")
    cerebro.addanalyzer(btanalyzers.SharpeRatio, timeframe=bt.TimeFrame.Minutes)
    cerebro.addanalyzer(btanalyzers.Returns, timeframe=bt.TimeFrame.Minutes)
    cerebro.addanalyzer(btanalyzers.Transactions)
    cerebro.addanalyzer(btanalyzers.TradeAnalyzer)
    cerebro.addanalyzer(btanalyzers.PositionsValue, headers=True)
    cerebro.addanalyzer(CashMarket)


def get_analyzers(strategy, market_config):
    logger.info("Collecting analyzers")
    # Get analysis data from cerebro
    sharpe = strategy.analyzers.sharperatio.get_analysis()
    returns = strategy.analyzers.returns.get_analysis()
    trade_analyzer = strategy.analyzers.tradeanalyzer.get_analysis()

    transactions = get_transactions(strategy)
    positions_value = get_positions_value(strategy)
    positions_size = get_positions_size(
        strategy, positions_value, transactions, market_config
    )

    # Setup quantstats session
    qs.extend_pandas()
    cash_market = strategy.analyzers.cashmarket.get_analysis()
    df_values = pd.DataFrame(cash_market).T
    df_values = df_values.iloc[:, 1]

    benchmark = get_benchmark(
        market_config.from_date, market_config.to_date, market_config.timeframe
    )
    greeks = qs.stats.greeks(df_values, benchmark)

    return {
        "returns": returns,
        "trade_analyzer": simplejson.loads(simplejson.dumps(trade_analyzer)),
        "sharpe": sharpe["sharperatio"],
        "transactions": transactions,
        "positions_value": positions_value,
        "position_size": positions_size,
        "alpha": float(greeks.alpha),  # numpy type
        "beta": float(greeks.beta),  # numpy type
        "broker": get_broker(strategy),
    }


def get_transactions(strategy):
    transactions = strategy.analyzers.transactions.get_analysis()
    return OrderedDict([(str(date), data) for date, data in transactions.items()])


def get_positions_value(strategy):
    positions_value = strategy.analyzers.positionsvalue.get_analysis()
    return OrderedDict([(str(date), data) for date, data in positions_value.items()])


def get_positions_size(strategy, positions_value, transactions, market_config):
    # https://community.backtrader.com/topic/1454/getposition-size-inside-bt-observer
    positions_size = OrderedDict()
    # Header
    positions_size["Datetime"] = list(positions_value["Datetime"])
    prev_date = ""
    index = dict(
        [(symbol, idx) for idx, symbol in enumerate(positions_value["Datetime"])]
    )

    for i, date in enumerate(positions_value.keys()):
        if i == 0:
            # Skip header
            continue
        if i == 1:
            # First tick
            positions_size[date] = [0 for symbol in market_config.symbols]
            prev_date = date
        if i > 1:
            # All following ticks
            positions_size[date] = [v for v in positions_size[prev_date]]
            prev_date = date
        for transaction in transactions.get(date, []):
            size = transaction[0]
            symbol = transaction[3]
            positions_size[date][index[symbol]] += size

    return positions_size


def get_broker(strategy):
    cash_market = strategy.analyzers.cashmarket.get_analysis()
    all_vals = [value[1] for value in cash_market.values()]
    return {
        "initial_value": all_vals[0],
        "intermediate_value": all_vals,
        "final_value": all_vals[-1],
    }

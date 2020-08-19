import logging
import sys
from collections import OrderedDict

import backtrader as bt
import backtrader.analyzers as btanalyzers
import pandas as pd
import quantstats as qs

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

    transactions = get_transactions(strategy)
    positions_value = get_positions_value(strategy)
    positions_size = get_positions_size(positions_value, transactions)

    return {
        "returns": get_returns(strategy),
        "trade_analyzer": get_trade_analyzer(strategy),
        "sharpe": get_sharpe(strategy),
        "transactions": transactions,
        "positions_value": positions_value,
        "position_size": positions_size,
        "quantstats": get_quantstats(strategy, market_config),
        "broker": get_broker(strategy),
    }


def get_transactions(strategy):
    transactions = strategy.analyzers.transactions.get_analysis()
    return OrderedDict([(str(date), data) for date, data in transactions.items()])


def get_positions_value(strategy):
    positions_value = strategy.analyzers.positionsvalue.get_analysis()
    return OrderedDict([(str(date), data) for date, data in positions_value.items()])


def get_positions_size(positions_value, transactions):
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
            positions_size[date] = [0 for symbol in positions_size["Datetime"]]
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


def get_returns(strategy):
    returns = strategy.analyzers.returns.get_analysis()
    return {
        "rtot": returns.get("rtot"),
        "ravg": returns.get("ravg"),
        "rnorm": returns.get("rnorm"),
        "rnorm100": returns.get("rnorm100"),
    }


def get_sharpe(strategy):
    return strategy.analyzers.sharperatio.get_analysis()["sharperatio"]


def get_trade_analyzer(strategy):
    trade_analyzer = strategy.analyzers.tradeanalyzer.get_analysis()
    # Normally this function just doesn't include any data when no trades happen.
    # This is a disaster for parsing so instead of the keyworks not existing they equal None
    return {
        "info": {
            "total": trade_analyzer.get("total", {}).get("total"),
            "open": trade_analyzer.get("total", {}).get("open"),
            "closed": trade_analyzer.get("total", {}).get("close"),
        },
        "streak": {
            "won": {
                "current": trade_analyzer.get("streak", {})
                .get("won", {})
                .get("current"),
                "longest": trade_analyzer.get("streak", {})
                .get("won", {})
                .get("longest"),
            },
            "lost": {
                "current": trade_analyzer.get("streak", {})
                .get("lost", {})
                .get("current"),
                "longest": trade_analyzer.get("streak", {})
                .get("lost", {})
                .get("longest"),
            },
        },
        "pnl": {
            "gross": {
                "total": trade_analyzer.get("pnl", {}).get("gross", {}).get("total"),
                "average": trade_analyzer.get("pnl", {})
                .get("gross", {})
                .get("average"),
            },
            "net": {
                "total": trade_analyzer.get("pnl", {}).get("net", {}).get("total"),
                "average": trade_analyzer.get("pnl", {}).get("net", {}).get("average"),
            },
        },
        "won": {
            "total": trade_analyzer.get("won", {}).get("total"),
            "pnl": {
                "total": trade_analyzer.get("won", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("won", {}).get("pnl", {}).get("average"),
                "max": trade_analyzer.get("won", {}).get("pnl", {}).get("max"),
            },
        },
        "lost": {
            "total": trade_analyzer.get("lost", {}).get("total"),
            "pnl": {
                "total": trade_analyzer.get("lost", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("lost", {}).get("pnl", {}).get("average"),
                "max": trade_analyzer.get("lost", {}).get("pnl", {}).get("max"),
            },
        },
        "long": {
            "total": trade_analyzer.get("long", {}).get("total"),
            "won": trade_analyzer.get("long", {}).get("won"),
            "lost": trade_analyzer.get("long", {}).get("lost"),
            "pnl": {
                "total": trade_analyzer.get("long", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("long", {}).get("pnl", {}).get("average"),
            },
        },
        "short": {
            "total": trade_analyzer.get("short", {}).get("total"),
            "won": trade_analyzer.get("short", {}).get("won"),
            "lost": trade_analyzer.get("short", {}).get("lost"),
            "pnl": {
                "total": trade_analyzer.get("short", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("short", {})
                .get("pnl", {})
                .get("average"),
            },
        },
    }


def get_quantstats(strategy, market_config):
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
        "alpha": float(greeks.alpha) if greeks.alpha else None,
        "beta": float(greeks.beta) if greeks.beta else None,
    }

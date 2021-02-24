import logging
import sys
from collections import OrderedDict

import backtrader as bt
import backtrader.analyzers as btanalyzers
import pandas as pd
import quantstats as qs

from ..feeds.utils import get_benchmark
from .cash_market import CashMarket
from .trade_list import TradeList

# Create logger
logger = logging.getLogger(__name__)


def add_analyzers(cerebro):
    logger.info("Adding analyzers to cerebro")
    cerebro.addanalyzer(btanalyzers.SharpeRatio, timeframe=bt.TimeFrame.Minutes)
    cerebro.addanalyzer(btanalyzers.Returns, timeframe=bt.TimeFrame.Minutes)
    cerebro.addanalyzer(btanalyzers.Transactions)
    cerebro.addanalyzer(btanalyzers.TradeAnalyzer)
    cerebro.addanalyzer(btanalyzers.PositionsValue, headers=True)
    cerebro.addanalyzer(CashMarket)
    cerebro.addanalyzer(TradeList)


def get_analyzers(strategy, market_config):
    logger.info("Collecting analyzers")

    transactions = get_transactions(strategy)
    positions = get_positions(strategy, transactions)

    return {
        "returns": get_returns(strategy),
        "trade_analyzer": get_trade_analyzer(strategy),
        "sharpe": get_sharpe(strategy),
        "transactions": transactions,
        "positions": positions,
        "quantstats": get_quantstats(strategy, market_config),
        "broker": get_broker(strategy),
        "trade_list": get_trade_list(strategy),
    }


def get_transactions(strategy):
    transactions = strategy.analyzers.transactions.get_analysis()
    parsed = dict()
    for date, row in transactions.items():
        dt = date.timestamp()
        parsed[dt] = dict()
        for cell in row:
            parsed[dt][cell[3]] = dict(
                position_size=cell[0],
                fill_price=cell[1],
                id=cell[2],
                symbol=cell[3],
                position_value=cell[4],
            )
    return parsed


def get_positions(strategy, transactions):
    positions_value = strategy.analyzers.positionsvalue.get_analysis()

    positions = dict()
    symbols = positions_value.pop("Datetime")
    old_dt = None
    for date, row in positions_value.items():
        dt = date.timestamp()
        positions[dt] = dict()

        # Create dict for symbol at date
        for idx, cell in enumerate(row):
            positions[dt][symbols[idx]] = dict()

        # Parse position value
        for idx, cell in enumerate(row):
            positions[dt][symbols[idx]]["value"] = value = cell
        # Parse position size
        for symbol in symbols:
            old_size = positions.get(old_dt, {}).get(symbol, {}).get("size", 0)
            new_row = transactions.get(dt, {})
            new_cell = new_row.get(symbol, {})
            new_size = new_cell.get("position_size", 0)
            positions[dt][symbol]["size"] = old_size + new_size

        old_dt = dt

    return positions


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


def get_trade_list(strategy):
    return strategy.analyzers.tradelist.get_analysis()


def get_trade_analyzer(strategy):
    trade_analyzer = strategy.analyzers.tradeanalyzer.get_analysis()
    # Normally this function just doesn't include any data when no trades happen.
    # This is a disaster for parsing so instead of the keyworks not existing they equal None
    return {
        "info": {
            "total": trade_analyzer.get("total", {}).get("total", 0),
            "open": trade_analyzer.get("total", {}).get("open", 0),
            "closed": trade_analyzer.get("total", {}).get("close", 0),
        },
        "streak": {
            "won": {
                "current": trade_analyzer.get("streak", {})
                .get("won", {})
                .get("current", 0),
                "longest": trade_analyzer.get("streak", {})
                .get("won", {})
                .get("longest", 0),
            },
            "lost": {
                "current": trade_analyzer.get("streak", {})
                .get("lost", {})
                .get("current", 0),
                "longest": trade_analyzer.get("streak", {})
                .get("lost", {})
                .get("longest", 0),
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
            "total": trade_analyzer.get("won", {}).get("total", 0),
            "pnl": {
                "total": trade_analyzer.get("won", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("won", {}).get("pnl", {}).get("average"),
                "max": trade_analyzer.get("won", {}).get("pnl", {}).get("max"),
            },
        },
        "lost": {
            "total": trade_analyzer.get("lost", {}).get("total", 0),
            "pnl": {
                "total": trade_analyzer.get("lost", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("lost", {}).get("pnl", {}).get("average"),
                "max": trade_analyzer.get("lost", {}).get("pnl", {}).get("max"),
            },
        },
        "long": {
            "total": trade_analyzer.get("long", {}).get("total", 0),
            "won": trade_analyzer.get("long", {}).get("won", 0),
            "lost": trade_analyzer.get("long", {}).get("lost", 0),
            "pnl": {
                "total": trade_analyzer.get("long", {}).get("pnl", {}).get("total"),
                "average": trade_analyzer.get("long", {}).get("pnl", {}).get("average"),
            },
        },
        "short": {
            "total": trade_analyzer.get("short", {}).get("total", 0),
            "won": trade_analyzer.get("short", {}).get("won", 0),
            "lost": trade_analyzer.get("short", {}).get("lost", 0),
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

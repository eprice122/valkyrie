import os
from copy import deepcopy
from datetime import datetime, timedelta
from random import randrange

import numpy as np
import pandas as pd
from backtrader import TimeFrame
from pymongo import MongoClient

from ..environ import environ


def get_benchmark(from_date, to_date, timeframe, symbol="SPY"):
    documents = get_documents(timeframe, from_date, to_date, symbol)
    document = documents.pop(0)

    parsed = dict()
    if timeframe == TimeFrame.Days:
        while True:
            parsed[document["date"]] = document["close"]
            if len(documents) > 0:
                document = documents.pop(0)
            else:
                break

    elif timeframe == TimeFrame.Minutes:
        to_date = datetime(year=to_date.year, month=to_date.month, day=to_date.day,)

        minutes = 0
        while True:
            if minutes == 0:
                current_date = datetime(
                    year=document["date"].year,
                    month=document["date"].month,
                    day=document["date"].day,
                    hour=9,
                    minute=30,
                    second=0,
                )
            elif minutes >= len(document["close"]):
                minutes = 0
                if len(documents) > 0:
                    document = documents.pop(0)
                    continue
                else:
                    break
            parsed[current_date] = document["close"][minutes]
            minutes += 1
            current_date += timedelta(minutes=1)
    else:
        raise ValueError

    return (
        pd.Series(parsed)
        .pct_change()
        .fillna(0)
        .replace([np.inf, -np.inf], float("NaN"))
        .dropna()
    )


def get_documents(timeframe, from_date, to_date, symbol):
    from_date = datetime.fromtimestamp(0, timezone.utc).replace(
        year=from_date.year, month=from_date.month, day=from_date.day
    )
    to_date = datetime.fromtimestamp(0, timezone.utc).replace(
        year=to_date.year, month=to_date.month, day=to_date.day
    )

    documents = list()
    if environ.get("unittest", False):
        current_date = deepcopy(from_date)
        while current_date < to_date:
            if current_date.weekday() > 4:  # Skip Saturday and Sunday
                pass

            if timeframe == TimeFrame.Minutes:
                documents.append(
                    {
                        "symbol": symbol,
                        "open": _create_random_array(),
                        "high": _create_random_array(),
                        "low": _create_random_array(),
                        "close": _create_random_array(),
                        "volume": _create_random_array(),
                        "date": current_date,
                    }
                )
            elif timeframe == TimeFrame.Days:
                documents.append(
                    {
                        "symbol": symbol,
                        "open": _create_random(),
                        "high": _create_random(),
                        "low": _create_random(),
                        "close": _create_random(),
                        "volume": _create_random(),
                        "date": current_date,
                    }
                )
            else:
                raise ValueError
            current_date += timedelta(days=1)
    else:
        client = MongoClient(
            host=environ["MONGO_HOST"],
            port=int(environ["MONGO_PORT"]),
            username=environ["MONGO_MARKET_USER"],
            password=environ["MONGO_MARKET_PWD"],
            authSource="admin",
        )
        db = client["stockDB"]
        if timeframe == TimeFrame.Minutes:
            collection = db["oneMinuteTicks"]
        elif timeframe == TimeFrame.Days:
            collection = db["oneDayTicks"]
        else:
            raise ValueError
        cursor = collection.find(
            {"symbol": symbol, "date": {"$gte": from_date, "$lt": to_date}}
        ).sort("date", 1)
        while cursor.alive:
            documents.append(cursor.next())
    return documents


def _create_random_array():
    return [_create_random() for _ in range(391)]  # 1 market day in minutes


def _create_random():
    return randrange(10, 100)

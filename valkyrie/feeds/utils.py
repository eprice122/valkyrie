import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from backtrader import TimeFrame
from pymongo import MongoClient


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
    client = MongoClient(
        host=os.environ["MONGO_HOST"],
        port=int(os.environ["MONGO_PORT"]),
        username=os.environ["MONGO_MARKET_USER"],
        password=os.environ["MONGO_MARKET_PWD"],
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
    documents = []
    while cursor.alive:
        documents.append(cursor.next())
    return documents

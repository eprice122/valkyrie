import os
from datetime import datetime, timedelta

from backtrader import TimeFrame, date2num
from backtrader.feed import DataBase
from pymongo import MongoClient


class MongoFeed(DataBase):
    def __init__(self, symbol: str):
        super().__init__()

        self.timeframe: TimeFrame = self.params.timeframe
        self.symbol = symbol

    def start(self):

        client = MongoClient(
            host=os.environ["MONGO_HOST"],
            port=int(os.environ["MONGO_PORT"]),
            username=os.environ["MONGO_MARKET_USER"],
            password=os.environ["MONGO_MARKET_PWD"],
            authSource="admin",
        )
        db = client["stockDB"]
        if self.timeframe == TimeFrame.Minutes:
            self.collection = db["oneMinuteTicks"]
        elif self.timeframe == TimeFrame.Days:
            self.collection = db["oneDayTicks"]
        else:
            raise ValueError
        self.cursor = self.collection.find(
            {
                "symbol": self.symbol,
                "date": {"$gte": self.params.fromdate, "$lt": self.params.todate},
            }
        )

        self.from_date = datetime(
            year=self.params.fromdate.year,
            month=self.params.fromdate.month,
            day=self.params.fromdate.day,
            hour=9,
            minute=30,
            second=0,
        )
        self.to_date = datetime(
            year=self.params.todate.year,
            month=self.params.todate.month,
            day=self.params.todate.day,
        )
        self.minutes = 0
        self.current_date = self.from_date
        self.document = None

    def stop(self):
        pass

    def _load(self):
        if not self.document and self.cursor.alive:
            self.document = self.cursor.next()

        if self.timeframe == TimeFrame.Minutes:
            if self.minutes >= len(self.document["open"]):
                self.minutes = 0
                self.current_date = datetime(
                    year=self.current_date.year,
                    month=self.current_date.month,
                    day=self.current_date.day,
                    hour=9,
                    minute=30,
                    second=0,
                )
                self.current_date += timedelta(days=1)
                if self.cursor.alive:
                    self.document = self.cursor.next()
                else:
                    return False

            self.lines.datetime[0] = date2num(self.current_date)
            self.lines.open[0] = self.document["open"][self.minutes]
            self.lines.high[0] = self.document["high"][self.minutes]
            self.lines.low[0] = self.document["low"][self.minutes]
            self.lines.close[0] = self.document["close"][self.minutes]
            self.lines.volume[0] = self.document["volume"][self.minutes]
            self.lines.openinterest[0] = 0
            self.minutes += 1
            self.current_date += timedelta(minutes=1)

        elif self.timeframe == TimeFrame.Days:
            if self.cursor.alive:
                self.document = self.cursor.next()
            else:
                return False
            self.lines.datetime[0] = date2num(self.current_date)
            self.lines.open[0] = self.document["open"]
            self.lines.high[0] = self.document["high"]
            self.lines.low[0] = self.document["low"]
            self.lines.close[0] = self.document["close"]
            self.lines.volume[0] = self.document["volume"]
            self.lines.openinterest[0] = 0
            self.current_date += timedelta(days=1)
        # Say success
        return True

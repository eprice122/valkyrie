import os
from datetime import datetime, timedelta
from threading import Event

from backtrader import TimeFrame, date2num
from backtrader.feed import DataBase

from .utils import get_documents


class VirtualFeed(DataBase):
    def __init__(self, symbol: str, interupt_handler: Event):
        super().__init__()
        self.timeframe: TimeFrame = self.params.timeframe
        self.symbol = symbol
        self.interupt_handler = interupt_handler

    def start(self):
        pass

    def stop(self):
        pass

    def _load(self):
        if self.interupt_handler.is_set():
            raise InterruptedError
        if self.timeframe == TimeFrame.Minutes:
            if self.minutes >= len(self.document["open"]):
                self.minutes = 0
                if len(self.documents) > 0:
                    self.document = self.documents.pop(0)
                else:
                    return False

            nine_thirty = 60 * 9.5
            self.lines.datetime[0] = date2num(
                self.document["date"] + timedelta(minutes=self.minutes + nine_thirty)
            )
            self.lines.open[0] = self.document["open"][self.minutes]
            self.lines.high[0] = self.document["high"][self.minutes]
            self.lines.low[0] = self.document["low"][self.minutes]
            self.lines.close[0] = self.document["close"][self.minutes]
            self.lines.volume[0] = self.document["volume"][self.minutes]
            self.lines.openinterest[0] = 0
            self.minutes += 1

        elif self.timeframe == TimeFrame.Days:
            if not self.document:
                return False
            self.lines.datetime[0] = date2num(self.document["date"])
            self.lines.open[0] = self.document["open"]
            self.lines.high[0] = self.document["high"]
            self.lines.low[0] = self.document["low"]
            self.lines.close[0] = self.document["close"]
            self.lines.volume[0] = self.document["volume"]
            self.lines.openinterest[0] = 0
            if len(self.documents) > 0:
                self.document = self.documents.pop(0)
            else:
                self.document = None

        # Say success
        return True

    def virtual_load(self):
        self.documents = get_documents(
            timeframe=self.timeframe,
            from_date=self.params.fromdate,
            to_date=self.params.todate,
            symbol=self.symbol,
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

        self.document = self.documents.pop(0)

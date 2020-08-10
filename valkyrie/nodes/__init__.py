import datetime

import backtrader as bt
import backtrader.feeds as btfeeds
import backtrader.indicators as btind


class TestStrategy(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        # print("%s, %s" % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.ema0 = btind.EMA(self.data.close, period=5)
        self.ema1 = btind.EMA(self.data.close, period=10)
        self.der = btind.Momentum(self.ema1, period=1)
        self.cross = btind.CrossUp(self.ema0, self.ema1)

    def next(self):
        self.log("Close, %.2f" % self.dataclose[0])
        if self.der[0] > 0 and self.cross[0] == 1:
            self.log("BUY CREATE, %.2f" % self.dataclose[0])
            self.buy(trailpercent=5)

    def stop(self):
        self.dataclose
        x = 0


if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.addstrategy(TestStrategy)

    # Create a Data Feed
    data = bt.feeds.GenericCSVData(
        dataname="data.csv",
        # Do not pass values before this date
        fromdate=datetime.datetime(2018, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2018, 1, 2),
        timeframe=bt.TimeFrame.Minutes,
        openinterest=-1,
    )

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final result
    print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())


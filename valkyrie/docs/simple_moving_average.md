# Simple Moving Average

A Simple Moving Average (SMA) calculates the average of all ticks between the current price and the lookback period. The longer the period is, the stronger the trend direction is. However, the longer the period, the more the indicator lags behind the current market price.

### Formula

$SMA= \frac{\alpha_0 + \alpha_1 + \alpha_2 + ... + \alpha_n}{n}$

__Where:__

$\ n$ = Lookback Period

$\alpha_n$ = Price at the n^th^ tick from current
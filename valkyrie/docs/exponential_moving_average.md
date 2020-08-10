# Exponential Moving Average

An Exponential Moving Average (EMA), similar to the Simple Moving Average (SMA) calculates the average of all ticks between the current price and the lookback period. However unlike the SMA, the EMA places an __exponentially__ larger weight on the most recent ticks.

### Formula

$EMA= \beta * (Current - EMA_{prev}) + EMA_{prev}$

__Where:__

$EMA_{prev}$ = Previous tick EMA

$Current$ = Current Price

$\beta$ = Smoothing constant
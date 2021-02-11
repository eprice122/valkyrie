# Exponential Moving Average

An Exponential Moving Average (EMA), similar to the Simple Moving Average (SMA) calculates the average of all ticks between the current price and the lookback period. However unlike the SMA, the EMA places an __exponentially__ larger weight on the most recent ticks. [Learn More](https://www.investopedia.com/terms/e/ema.asp)

## Formula

$EMA= \beta * (Current - EMA_{prev}) + EMA_{prev}$

- $EMA_{prev}$ = Previous tick EMA

- $Current$ = Current Price

- $\beta$ = Smoothing constant

## Example

![](https://doc-assets-k7d4.s3.amazonaws.com/ema-indicator.png)

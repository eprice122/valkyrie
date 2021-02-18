# Bollinger Bands (BB)

Measures volatility by predicting an overbought (top band) and oversold (bottom band) market. The closer the current price to the band, the more overbought/sold the stock is. [Learn More](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/bollinger-bands)

_Default Period = 30_

_Default Dev Factor = 2_

## Formula

$MID = SMA(close,n)$

$TOP = MID + \alpha * SMA(input, n)$

$TOP = MID - \alpha * SMA(input, n)$
* $\alpha$ = dev factor
* $n$ = period

## Example
![](https://doc-assets-k7d4.s3.amazonaws.com/bb-indicator.png)

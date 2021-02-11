# Weighted Moving Average (WMA)

A Weighted Moving Average, similar to the Simple Moving Average (SMA) calculates the average of all ticks between the current price and the lookback period. However unlike the SMA, the WMA places a __linearly__ larger weight on the most recent ticks. [Learn More](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/wma)

## Formula

$WMA= \frac{\alpha_o * (n) + \alpha_1 * (n-1) + \alpha_2 * (n-2) + ... \alpha_n * (1)}{n + (n-1) + (n-2) + (n-3) + ...1}$

- $alpha_n$ = Price n ticks ago

- $n$ = Lookback period

## Example

If $n$ = 4:

$WMA= \frac{\alpha_o * (4) + \alpha_1 * (3) + \alpha_2 * (2) + \alpha_n * (1)}{5 + 4 + 3 + 2 + 1}$

![](https://doc-assets-k7d4.s3.amazonaws.com/wma-indicator.png)

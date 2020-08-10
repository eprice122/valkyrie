# Weighted Moving Average

A Weighted Moving Average (WMA), similar to the Simple Moving Average (SMA) calculates the average of all ticks between the current price and the lookback period. However unlike the SMA, the WMA places a __linearly__ larger weight on the most recent ticks.

### Formula

$WMA= \frac{\alpha_o * (n) + \alpha_1 * (n-1) + \alpha_2 * (n-2) + ... \alpha_n * (1)}{n + (n-1) + (n-2) + (n-3) + ...1}$

__Where:__

$alpha_n$ = Price n ticks ago

$n$ = Lookback period

__Example:__

If $n$ = 4:

$WMA= \frac{\alpha_o * (4) + \alpha_1 * (3) + \alpha_2 * (2) + \alpha_n * (1)}{5 + 4 + 3 + 2 + 1}$
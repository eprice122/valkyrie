# Triple Exponential Moving Average (TEMA)

A Triple Exponential Moving Average is an adaptation of the [exponential moving average](https://docs.hedgehog.market/libraries/average/#exponential_moving_average) with the ambition of reducing the lag moving averages fundamentally contain. [Learn More](https://www.investopedia.com/terms/t/triple-exponential-moving-average.asp)

## Formula

$TEMA= (3 * EMA_0) - (3 * EMA_1) + (3 * EMA_2)$

- $\ n$ = Lookback Period

- $EMA_0 = EMA(input, n)$

- $EMA_1 = EMA(EMA_0, n)$

- $EMA_2 = EMA(EMA_1, n)$

## Example

![](https://doc-assets-k7d4.s3.amazonaws.com/tema-indicator.png)
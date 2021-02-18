# Relative Strength Index (RSI)

Measures momentum by calculating the ration of higher closes and lower closes after having been smoothed by an average, normalizing the result between 0 and 100. [Learn More](https://en.wikipedia.org/wiki/Relative_strength_index)

## Formula

$RSI = 100 - 100 / (1 + \frac{ma_{up}}{ma_{do}})$

* $U$ = up_day(input)
* $D$ = down_day(input)
* $ma_{up}$ = moving_average($U$)
* $ma_{do}$ = moving_average($D$)

## Example
![](https://doc-assets-k7d4.s3.amazonaws.com/rsi-indicator.png)

_Note the data is normalized between -1 and 1._
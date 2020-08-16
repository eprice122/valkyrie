# RSI

Measures momentum by calculating the ration of higher closes and lower closes after having been smoothed by an average, normalizing the result between 0 and 100.

### Formula

$RSI = 100 - 100 / (1 + \frac{ma_{up}}{ma_{do}})$

__Where:__

$U$ = up_day(input)
$D$ = down_day(input)

$ma_{up}$ = moving_average($U$)
$ma_{do}$ = moving_average($D$)
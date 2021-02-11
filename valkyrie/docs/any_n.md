# Any Previous (ANYN)

## Output
> If - __True__ if _any_ the previous input ticks of the period are not 0. Else __False__.
> 
> If - __False__ if _any_ the previous input ticks of the period are not 0. Else __True__.
> 
__Example__

_Any N with a period of 5._


| Tick    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|
| Price   | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0  | 0  | 0  | 0  | 0  |
| AnyN(5) | x | x | x | x | 1 | 1 | 0 | 0 | 1 | 1 | 1  | 1  | 1  | 0  | 0  |
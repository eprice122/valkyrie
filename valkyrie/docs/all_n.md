# All Previous (ALLN)

## Output
> If - __True__ if _all_ the previous input ticks of the period are not 0. Else __False__.
> 
> If - __False__ if _all_ the previous input ticks of the period are not 0. Else __True__.

## Example

_All N with a period of 5._

| Tick    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---------|---|---|---|---|---|---|---|---|---|---|----|----|----|
| Price   | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1  | 1  | 0  |
| AllN(5) | x | x | x | x | 0 | 0 | 0 | 1 | 1 | 0 | 0  | 0  | 0  |
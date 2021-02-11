# Lookback (LB)


Outputs the value of the input N ticks back in time.

## Example

_Lookback with period of 5_

| Tick  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|---|
| Price | 2 | 3 | 4 | 3 | 6 | 4 | 3 | 2 | 5 |
| LB(5) | x | x | x | x | 2 | 3 | 4 | 3 | 6 |
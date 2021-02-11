# Lowest Index (LOI)

Returns the index of the first data that is the lowest in the period.

## Example

_Lowest Index with period of 4_

| Tick  | 0  | 1  | 2 | 3 | 4 | 5 | 6  | 7  | 8  | 9 | 10 | 11 | 12 |
|-------|----|----|---|---|---|---|----|----|----|---|----|----|----|
| Price | 10 | 12 | 8 | 9 | 5 | 7 | 13 | 10 | 11 | 9 | 12 | 13 | 4  |
| LOI(4) | x  | x  | x | 1 | 0 | 1 | 2  | 3  | 3  | 0 | 1  | 2  | 0  |
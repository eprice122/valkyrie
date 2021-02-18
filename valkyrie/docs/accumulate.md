# Accumulate (ACCU)

Keeps a running total of all previous values. Useful for testing how often logic is positive or negative.

| Tick   | 0 | 1 | 2  | 3 | 4  | 5  | 6  | 7 | 8 |
|--------|---|---|----|---|----|----|----|---|---|
| Price  | 2 | 3 | -1 | 4 | -6 | -3 | -1 | 2 | 5 |
| ACCU() | 2 | 5 | 4  | 8 | 2  | -1 | -2 | 0 | 5 |
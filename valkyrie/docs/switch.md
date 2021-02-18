# Switch (SW)

Gate which outputs __zero__ if state is __True__ and __Input__ if state is __False__


## Example
| Tick   | 0 | 1 | 2 | 3 | 4 | 5  | 6  | 7 | 8 |
|--------|---|---|---|---|---|----|----|---|---|
| STATE  | 0 | 0 | 0 | 1 | 1 | 0  | 1  | 0 | 1 |
| INPUT  | 2 | 5 | 4 | 8 | 2 | -1 | -2 | 0 | 5 |
| OUTPUT | 0 | 0 | 0 | 8 | 2 | 0  | -2 | 0 | 5 |
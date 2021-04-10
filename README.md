# Valkyrie

_The official wrapper api for [Hedgehog.market](https://hedgehog.market) to convert indicator graphs into python scripts [Backtrader](https://www.backtrader.com)._

<img src=https://github.com/eprice122/valkyrie/actions/workflows/tests.yml/badge.svg>

## Current Indicators Available

__Fundamental__
- [Crossover](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/crossover.md)
- [Math](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/math.md)
- [Or Logic](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/or_logic.md)
- [And Logic](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/and_logic.md)
- [All N](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/all_n.md)
- [Any N](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/any_n.md)
- [Sum N](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/sum_n.md)
- [Lookback](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/lookback.md)
- [Rank](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/rank.md)
- [Switch](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/switch.md)
- [Constant](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/constant.md)
- [Accumulate](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/accumulate.md)
- [Default Value](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/default_value.md)
- [Absolute Value](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/absolute_valu.md)

__Average__
- [Simple Moving Average](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/simple_moving_average.md)
- [Simple Moving Average Envelope](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/simple_moving_average_env.md)
- [Exponential Moving Average](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/exponential_moving_average.md)
- [Weighted Moving Average](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/weighted_moving_average.md)
- [True Range](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/true_range.md)
- [Average True Range](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/average_true_range.md)
- [Triple Exponential Moving Average](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/triple_ema.md)

__Extrema__
- [Lowest Value](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/lowest_value.md)
- [Highest Value](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/highest_value.md)
- [Lowest Index](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/lowest_index.md)
- [Highest Index](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/highest_index.md)

__Momentum__
- [Commodity Channel Index](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/commodity_channel_index.md)
- [Rate of Change](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/rate_of_change.md)
- [Relative Strength Index](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/rsi.md)
- [Derivative](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/derivative.md)
- [Bollinger Bands](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/bollinger_bands.md)


__Statistics__
- [Mean Deviation](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/mean_deviation.md)
- [Standard Deviation](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/standard_deviation.md)

__Order__
- [Market Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/market_order.md)
- [Stop Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/stop_order.md)
- [Limit Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/limit_order.md)
- [Stop Limit Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/stop_limit_order.md)
- [Stop Trail Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/stop_trail_order.md)
- [Limit Bracket Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/limit_bracket_order.md)
- [Market Bracket Order](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/market_bracket_order.md)


__Data__
- [Equities](https://github.com/eprice122/valkyrie/blob/master/valkyrie/docs/equities.md)

---

## Contributing An Indicator

All indicators are written to be compatible with the Backtrader api.

__Steps:__

1. Create the indicator following the same design patterns as the existing ones
2. Create the markdown documentation in the docs directory
3. Build the parsing method. Example:
```
simple_moving_average_docs = Node(
    key="simple_moving_average",
    label="Simple Moving Average",
    type="INDICATOR_NODE",
    tooltip="Non-weighted average of the last n periods.",
    docs_path="simple_moving_average.md",
    parameters=[Parameter(key="period", label="Period", ui=IntegerUI())],
    inputs=[Input(key="input0")],
    outputs=[Output()],
)
```
4. Add basic unit test to the respective test suite
5. Submit a pull request to be approved
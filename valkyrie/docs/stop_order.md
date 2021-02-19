# Stop Order

An order type which triggers a market order when the price crosses specified value. [Learn More](https://www.investopedia.com/terms/s/stoporder.asp)

* Stop orders can be used to mitigate risk via setting a stop loss

## Parameters

### Side \<Selection>
> Direction of order.
>
> * Options: Buy, Sell

### Size \<Integer>
> Quantity of shares to perform order operation on.
>
> * Must be greater than zero

### Stop Percent \<Float>
> Percent from close (when order placed) to trigger order.
>
> * Must be _greater_ than zero when _buy_ side
> * Must be _less_ than zero when _sell_ side

## Example

### Buy Limit Order

| Parameter     | Value |
|---------------|-------|
| Side          | Buy   |
| Size          | 100   |
| Stop Percent  | -0.5  |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a stop order will be executed to trigger a [market buy order](https://docs.hedgehog.market/libraries/standard_order/#market_order) at $149.25 (0.995 * 150.00).

### Sell Limit Order

| Parameter     | Value  |
|---------------|--------|
| Side          | Sell   |
| Size          | 100    |
| Stop Percent  | 1.0    |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a stop order will be executed to trigger a [market sell order](https://docs.hedgehog.market/libraries/standard_order/#market_order) at $151.50 (1.01 * 150.00).


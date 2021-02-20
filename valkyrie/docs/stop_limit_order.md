# Stop Limit Order

An order which triggers a _limit_ order when the price crosses specified value. [Learn More](https://www.investopedia.com/terms/s/stop-limitorder.asp)

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

### Limit Percent \<Float>
> Percent from close (when order placed) to trigger order.
> 
> * Must be _less_ than zero when _buy_ side
> * Must be _greater_ than zero when _sell_ side

## Example

### Buy Stop Limit Order

| Parameter     | Value |
|---------------|-------|
| Side          | Buy   |
| Size          | 100   |
| Stop Percent  | -0.5  |
| Limit Percent | -0.4  |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a stop order will be executed to trigger a [limit buy order](https://docs.hedgehog.market/libraries/standard_order/#market_order) at \$149.25 (0.995 * 150.00). This limit order will have a buy limit at \$149.40 (0.9975 * 150.00)

### Sell Stop Limit Order

| Parameter     | Value  |
|---------------|--------|
| Side          | Sell   |
| Size          | 100    |
| Stop Percent  | 0.6    |
| Limit Percent | -0.3   |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a limit order will be executed to trigger a [limit sell order](https://docs.hedgehog.market/libraries/standard_order/#market_order) at \$150.90 (1.006 * 150.00). This limit order will have a sell limit at \$149.55 (0.997 * 150.00)


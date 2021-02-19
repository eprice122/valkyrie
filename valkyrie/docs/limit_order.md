# Limit Order

An order type which only fills if the price is equal or better than the limit price. [Learn More](https://www.investopedia.com/terms/l/limitorder.asp)

* Useful for low volume or highly volatile stocks

## Parameters

### Side \<Selection>
> Direction of order.
>
> * Options: Buy, Sell

### Size \<Integer>
> Quantity of shares to perform order operation on.
>
> * Must be greater than zero

### Limit Percent \<Float>
> Percent from close (when order placed) to trigger order.
> 
> * Must be _less_ than zero when _buy_ side
> * Must be _greater_ than zero when _sell_ side

## Example

### Buy Limit Order

| Parameter     | Value |
|---------------|-------|
| Side          | Buy   |
| Size          | 100   |
| Limit Percent | -0.5  |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a limit order will be executed to buy at $149.25 (0.995 * 150.00).

### Sell Limit Order

| Parameter     | Value  |
|---------------|--------|
| Side          | Sell   |
| Size          | 100    |
| Limit Percent | 1.0    |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a limit order will be executed to sell at $151.50 (1.01 * 150.00).


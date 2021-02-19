# Stop Trail Order

An order which follows the trend (direction depends on parameters), and triggers a market order when the trend reverses by a specified amount. [Learn More](https://www.investopedia.com/terms/t/trailingstop.asp)

* This type of order is used to guarentee profits
* Trailing stop loses placed too close to the trend can exit early losing potential gains

## Parameters

### Side \<Selection>
> Direction of order.
>
> * Options: Buy, Sell

### Size \<Integer>
> Quantity of shares to perform order operation on.
>
> * Must be greater than zero

### Trail Percent \<Float>
> Percent from close (when order placed) to trail order from.
> 
> * Must be greater than zero

### Buy Stop Trail Order

| Parameter     | Value |
|---------------|-------|
| Side          | Buy   |
| Size          | 100   |
| Trail Percent | -0.5  |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a stop trail order will be executed. The stop price proceeds to follow the price by the _trail percentage_. __If__ the equity price increases above this threshold, __then__ a [market buy order](https://docs.hedgehog.market/libraries/standard_order/#market_order) will be placed.

### Sell Stop Limit Order

| Parameter     | Value  |
|---------------|--------|
| Side          | Sell   |
| Size          | 100    |
| Trail Percent | 0.5   |

__If__ the current closing price is \$150.00 and an order is triggered __then__ a stop trail order will be executed. The stop price proceeds to follow the price by the _trail percentage_. __If__ the equity price decreases below this threshold, __then__ a [market sell order](https://docs.hedgehog.market/libraries/standard_order/#market_order) will be placed.
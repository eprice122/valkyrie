# Limit Bracket Order

- [x] In development

An order type which, on trigger, executes a limit order along with a lower and upper order.

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

### Upper Order Type \<Selection>
> Order type for upper band.
>
> * Options: Limit Order, Stop Order, Stop Trail Order

### Upper Trigger \<Float>
> Percent from close (when order placed) to trigger order.

### Lower Order Type \<Selection>
> Order type for lower band.
>
> * Options: Limit Order, Stop Order, Stop Trail Order

### Lower Trigger \<Float>
> Percent from close (when order placed) to trigger order.
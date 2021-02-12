# True Range (TR)

A true range measures market volitility of each tick using the high, low, and yesterday's close. This indicator is often used as a predecessor for a simple moving average.

* Large TR = higher volitility

* Lower TR = lower volitility

## Formula

$TR = Max[Abs(H - C_p), Abs(L - C_p), (H - L)]$

- $H$ = High

- $L$ = Low

- $C_p$ = Previous Close

## Example

![](https://doc-assets-k7d4.s3.amazonaws.com/tr-indicator.png)

Note this is normalized data between -1 and 1. Volume bars are displayed to compare volitility.
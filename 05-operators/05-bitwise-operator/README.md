## Bitwise Operators

Bitwise operators are used to perform bit-level operations on integers. They operate on the binary representations of numbers, manipulating individual bits.

## Bit

All data used or handled by computers is converted to binary format. A **bit** is the smallest unit of data in a computer, and it can be either `0` or `1`.

Here are the bitwise operators in Python:

```py
| Operator     | Symbol | Description                                                    | Example                   | Result        |
|--------------|--------|----------------------------------------------------------------|---------------------------|---------------|
| AND          | `&`    | Performs a bitwise AND operation                               | `5 & 3` (`0101 & 0011`)    | `1` (`0001`) |
| OR           | `|`    | Performs a bitwise OR operation                                | `5 | 3` (`0101 | 0011`)     | `7` (`0111`) |
| XOR          | `^`    | Performs a bitwise XOR operation                               | `5 ^ 3` (`0101 ^ 0011`)    | `6` (`0110`) |
| NOT          | `~`    | Performs a bitwise NOT operation (inverts all bits)            | `~5` (`~0101`)             | `-6`          |
| Left Shift   | `<<`   | Shifts the bits of the number to the left by the specified amount | `5 << 1` (`0101 << 1`)     | `10` (`1010`)|
| Right Shift  | `>>`   | Shifts the bits of the number to the right by the specified amount| `5 >> 1` (`0101 >> 1`)     | `2` (`0010`) |

```

### How Bitwise Operators Work:

- **AND (`&`)**: Each bit is compared between two numbers. If both bits are `1`, the result is `1`; otherwise, it’s `0`.
- **OR (`|`)**: If at least one bit is `1` between two numbers, the result is `1`.
- **XOR (`^`)**: If the bits differ (one is `1` and the other is `0`), the result is `1`;if two bits are same, output is `0`.
- **NOT (`~`)**: Inverts each bit, turning `0` into `1` and vice versa.
- **Left Shift (`<<`)**: Shifts all bits to the left by a certain number of positions, filling the rightmost bits with `0`.
- **Right Shift (`>>`)**: Shifts all bits to the right by a certain number of positions, discarding the rightmost bits.

## AND, OR, NOT

```py
a = 2
b = 3
print("{a} & {b}}", a&b) # 2

a = 2 = 010
b = 3 = 110
a and b=010 = 3
print("{a} | {b}", a|b) # 3
```

## Not operator

It flips each bit to its opposite and also it converts our number to its opposite side.
In our computers memory, we store the numbers along with their sign, the left most bit represents the sign of the number, if it is `0`, it means it is a positive integer, if it is `1`, it means it is a negative value.
Flipping the bit means that bit is also going to be flipped, thus changing the sign.

```py
a = 2
print(~a) # -3

```

## Left shift a<<x

We shift our binary numbers to the left by x amount, x represents the number of `0` we will append to the right.
It multiply our number by 2.

```py
a = 6
a = 110
a<<1 = 1100 = 12 # shift a by 1, means append only one `0` to the right
a<<2 = 11000 = 24
a<<2 = 110000 = 48

```

## Right shift a>>x

It removes the right bits by x amount.
It divide our divides our result by 1 on each shift.

```py
a = 6
a = 110
a>>1 = 11 = 3 # shift a by 1, means remove one bit from right side
a>>2 = 1 = 1
```

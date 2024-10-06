Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division on numbers.

There are 7 arithmetic operators in Python :

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation
- Floor division

```table
| Operator       | Symbol | Description                          | Example          | Result         |
|----------------|--------|--------------------------------------|------------------|----------------|
| Addition       | `+`    | Adds two numbers                     | `5 + 3`          | `8`            |
| Subtraction    | `-`    | Subtracts the second number from the first | `5 - 3`          | `2`            |
| Multiplication | `*`    | Multiplies two numbers               | `5 * 3`          | `15`           |
| Division       | `/`    | Divides the first number by the second | `5 / 2`          | `2.5`          |
| Modulus        | `%`    | Returns the remainder of division    | `5 % 2`          | `1`            |
| Exponentiation | `**`   | Raises the first number to the power of the second | `5 ** 3` | `125`          |
| Floor division | `//`   | Divides and returns the integer part of the quotient | `5 // 2` | `2`            |

```

## Precedence

All operator does not hold the same level of precedence, some should be evaluated before others.

Here are some operators from lowest to highest precedence

```text
+, - (Addition, Subtraction)
*, /, //, % (Multiplication, Division, Floor Division, Modulus)
** (Exponentiation)
```

```py
print(3+5*3) # 18
print(-2+3**2) # 7
```

## Associativity

When the operators are having same level of precedence, we use associativity rule.
It specify from which side, we should start performing the operations.

````plaintext
```text
+, - (Addition, Subtraction). [Left to Right]
*, /, //, % (Multiplication, Division, Floor Division, Modulus) [Left to Right]
** (Exponentiation) [Right to Left]
````

```py
print(2+2) = 4
print(3-2-1) = 0
print(2**3**2) # print(2**9) = 512
```

## ()

When using `()`, associativity rule does not matter.

```py
print((2**3)**2) # print(8**1) = 64
```

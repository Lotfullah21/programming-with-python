## Decimal to binary

We can use `bin` built-in function to convert a decimal to binary and it returns a string.

```py
def decToBin(n):
    res = bin(n)
    return res

n = int(input("Enter an integer: "))
res = decToBin(n)
print(res, type(res))

```

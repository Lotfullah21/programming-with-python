## Returning multiple values

We can return multiple values from a function and when we return multiple values from a function, it will wrapped inside a tuple.
either through indexing or unpacking, we can get access to those values.

```py
def operations(x, y):
    total = x + y
    sub = x - y
    div = x//y
    return total, sub, div

# Unpacking
total, sub, div  = operations(12, 12)
print(total, sub, div)
# Through indexing.
x = operations(12,12)
print(x)
print("total =",x[0])
print("diff =",x[1])
print("div =",x[2])
```

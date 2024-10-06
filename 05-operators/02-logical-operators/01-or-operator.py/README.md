## Short circuit

in `and` operator, if one of the expression evaluates to false, the rest of the expression will be evaluated.

For instance,

```py
print(1<0 and 2>1)
```

Now, the `1<0` is enough to terminate the evaluation and return false.

## Logical operator with an integer value

If the value is non-zero, it is treated as True and if it is==0, it is tread as false.

```py
a = 10
print(a or 9) # 10

b = 0
print(b or a) # 10

print(a and b) # 0
```

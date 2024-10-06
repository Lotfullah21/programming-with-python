### Implicit

implicit conversion happens based on some pre defined rules in python, for instance there is a rule that if one of the data type is `int` and the other is `float`, the output should be in float.

```py
a = 10
b = 12.4
sum = a + b
print(sum) # 22.4
```

#### Boolean

`True` automatically gets converted to integer `1` and `False` automatically gets converted to `0`.

```py
sum = True + 10
print(sum) # 11
sum = False + 10
print(sum) # 10
print(False+11.2) # 11.2
```

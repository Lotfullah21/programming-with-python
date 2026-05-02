# Implicit Conversion

Implicit conversion happens when Python automatically converts one type to another during an operation.

Python only does this when the conversion is predictable and safe enough. For example, adding an `int` and a `float` gives a `float`.

```python
a = 10
b = 12.4
total = a + b

print(total)        # 22.4
print(type(total))  # <class 'float'>
```

## Booleans In Arithmetic

`True` behaves like `1`, and `False` behaves like `0` in arithmetic expressions.

```python
print(True + 10)     # 11
print(False + 10)    # 10
print(False + 11.2)  # 11.2
```

This is useful to know, but beginner code is usually clearer when you write the condition explicitly instead of relying on boolean arithmetic.

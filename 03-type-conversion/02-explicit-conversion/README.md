# Explicit Conversion

Explicit conversion means you ask Python to convert a value by calling a type constructor.

Common constructors:

- `int(value)`
- `float(value)`
- `str(value)`
- `bool(value)`
- `list(value)`
- `tuple(value)`
- `set(value)`

## Input Example

`input()` always returns a string.

```python
age_text = input("Age: ")
age = int(age_text)

print(age + 1)
```

## Failed Conversion

Not every value can be converted.

```python
int("12")   # works
int("abc")  # ValueError
```

Convert only after checking that the value has the form you expect.

# 03. Type Conversion

Type conversion means changing a value from one type to another. Python does this in two ways.

| Kind | Folder | Meaning |
| --- | --- | --- |
| Implicit conversion | [01-implicit-conversion](01-implicit-conversion/README.md) | Python converts safely for you during an operation |
| Explicit conversion | [02-explicit-conversion](02-explicit-conversion/README.md) | You call a constructor such as `int`, `float`, `str`, or `bool` |

## Example

```python
age_text = "21"
age = int(age_text)
print(age + 1)  # 22
```

## Rule Of Thumb

If data comes from `input()`, it starts as a string. Convert it before doing arithmetic.

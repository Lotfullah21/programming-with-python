# Range

`range` creates an immutable sequence of integers. It does not build a list immediately, but you can convert it to a list when you want to inspect every value.

## `range(stop)`

Starts at `0` and stops before `stop`.

```python
x = range(5)
print(x)        # range(0, 5)
print(type(x))  # <class 'range'>
print(list(x))  # [0, 1, 2, 3, 4]
```

## `range(start, stop)`

Starts at `start` and stops before `stop`.

```python
x = range(1, 5)
print(list(x))  # [1, 2, 3, 4]
```

```python
x = range(-2, 2)
print(list(x))  # [-2, -1, 0, 1]
```

## `range(start, stop, step)`

Uses `step` as the amount to move each time.

```python
x = range(1, 5, 2)
print(list(x))  # [1, 3]
```

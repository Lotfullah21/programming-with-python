# While Loop

A `while` loop repeats a block as long as a condition is `True`.

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## When To Use It

Use `while` when the number of repetitions is not known in advance.

Examples:

- keep asking for input until it is valid
- keep dividing a number until it becomes `0`
- keep running until a user chooses to exit

## Avoid Infinite Loops

Every `while` loop needs a condition that eventually becomes `False`.

This loop stops:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

This loop does not stop because `i` never changes:

```python
i = 0
while i < 5:
    print(i)
```

## `break` And Loop `else`

Use `break` to exit early.

```python
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
```

A loop `else` block runs only when the loop finishes normally, without hitting `break`.

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("done")
```

# List Introduction

A list is useful when you want to keep many related values under one name.

```python
fruits = ["apple", "banana", "grapes", "orange"]
numbers = [1, 2, 3, 4, 5]
```

## Mutation

Lists are **mutable**. You can change their contents after creation.

```python
fruits = ["apple", "banana", "grapes"]
fruits[1] = "pear"
fruits.append("orange")

print(fruits)  # ['apple', 'pear', 'grapes', 'orange']
```

## Files

- `01-intro.py`: creates simple lists.
- `02-mutation.py`: changes list values.
- `03-creating-and-accessing.py`: creates, indexes, appends, and reverses lists.

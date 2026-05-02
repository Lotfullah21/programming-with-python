# Sets

A set stores unique values. Sets are useful for removing duplicates and checking membership quickly.

```python
numbers = {1, 2, 2, 3}
print(numbers)      # {1, 2, 3}
print(2 in numbers) # True
```

## Lessons

| Lesson | Folder | Main idea |
| --- | --- | --- |
| 1 | [01-intro](01-intro/README.md) | Create sets and understand uniqueness |
| 2 | [02-operations](02-operations/README.md) | Add, remove, union, intersection, and difference |

## Important Details

- Sets are unordered.
- Sets do not support indexing.
- Set elements must be hashable, such as strings, numbers, booleans, or tuples.
- Use `set()` for an empty set. `{}` creates an empty dictionary.

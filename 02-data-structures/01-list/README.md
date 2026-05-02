# Lists

A list stores an ordered collection of values. Lists are mutable, which means you can add, remove, or replace elements after the list is created.

```python
fruits = ["apple", "banana", "grapes"]
fruits.append("orange")
print(fruits[0])      # apple
print(fruits[-1])     # orange
```

## Lessons

| Order | Folder | Focus |
| --- | --- | --- |
| 1 | [01-intro](01-intro/README.md) | Creating lists and mutation |
| 2 | [02-indexing](02-indexing/README.md) | Accessing values by position |
| 3 | [03-methods](03-methods/README.md) | Common list methods |
| 4 | [04-copy](04-copy/README.md) | Copying and slicing |
| 5 | [05-comprehension](05-comprehension/README.md) | Building lists with expressions |
| 6 | [06-problems](06-problems) | Practice problems |
| 7 | [07-practice](07-practice/README.md) | Extra examples from the old list notes |

## Remember

- Indexing returns one value: `fruits[0]`.
- Slicing returns a new list: `fruits[0:2]`.
- Assignment through an index mutates the list: `fruits[1] = "pear"`.
- `append` adds one item; `extend` adds each item from another iterable.

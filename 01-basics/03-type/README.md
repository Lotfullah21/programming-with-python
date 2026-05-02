## Types

types are automatically assigned to variables, we not need to specify type of variables.

### None

None is a special type in python, when we specify the type as none, it means we don't the value yet or no value is assigned to this variable.

## Iterables

iterables are objects that can be iterated (or looped) over. An iterable provides a sequence of elements, one at a time, allowing you to loop through its values

an iterable object implements the `__iter__()` method, which returns an iterator (an object that can keep track of its position during iteration).

## Indexing

`Strings`,`Lists`, and `Tuples` support indexing.

```py
newList = [1, 2, 3, 4]
print(newList[0])  # Output: 1
print(newList[3])  # Output: 4

```

```py
newTuple = (1, 2, 3, 4)
print(newTuple[0])  # Output: 1
print(newTuple[2])  # Output: 3

```

## Non indexing

The iterables that do not support indexing does not have a defined order like sets or dictionaries

`Sets` and `Dictionaries` do not support indexing.

```py
newSet = {1, 2, 3}
# print(newSet[0])  # This will raise a TypeError: 'set' object is not subscriptable

```

```py
newDict = {1: "a", 2: "b", 3: "c"}
print(newDict[1])  # Output: 'a'  (Access by key, not by index)
```

## Sequences

Sequences are not individual item, but a collection of smaller items, for instance `strings`, they are sequence of characters.

### List

[]

- ordered collection of items
- mutable, it means that once the items are added, they can be removed, modified.

```py
newList = [1,2,3,4,"10"]
print(type(newList))
```

### Tuple

()

- ordered collection of items
- not mutable, once it is created, no items can removed or modified from the tuple
- Tuples themselves are immutable, meaning you cannot modify their elements in place.
- but we can create a new tuple by adding a new tuple to the original tuple

```py
newTuple = (1,2,3,4,5)
# Creating a new tuple
newTuple = newTuple + (12,10,)
print(type(newTuple))
print(newTuple)
```

### Set

{}

- unordered collection of items
- each item should be unique, not duplicates are allowed.
- immutable
- uses hash function internally

```py
newSet = {1,2,3}
print(type(newSet))
newSet = set([1, 2, 3])
print(type(newSet))
print(newSet)
```

### Dictionary

- unordered collection of items
- mutable
- uses hash function internally
- the keys should be unique

```py
a = {1:"1",b:"12"}
print(type(a))
print(a)
```

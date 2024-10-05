## set()

A collection of element which are

- Distinct
- Unordered
- No indexing
- Union, intersection and difference are fast
- Uses hashing internally

We can create sets using a symbol (`{}`) and a function `set()`.

## 1. Symbol {}

Add the element inside `{}` with comma in between them.

```py
s1 = {1,2,3,4}
```

## 2. set()

Add a collection of element inside `set()`, these collections can be `tuple, list, dictionary.`

```py
s1 = set([1,2,3,4])
```

## Empty set

To create an empty set, we cannot use `{}`, because it is used for dictionaries as well, hence we use `set()` function to create an empty dictionary.

```py
s0 = set()
print(type(s0))

s0 = {}
print(s0)
```

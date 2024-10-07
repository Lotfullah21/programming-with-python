## Slicing

We can create a slicing slice a list using the following format.

syntax:

```py
list[starting index:ending index:incrementing step]
```

If we do not add `step` value, it will be considered as 1.

```py
l1 = [1,2,3,4,5,6,7,8,9]
print(l1)
print(l1[1:5])
print(l1[1:5:1])
```

## copy

We can create a new list using slicing

```py
newlist = prevlist[:]
```

For list, it will create a new list, but for tuples and string, both of the sequences will be referencing to the same object in memory, because of their immutable nature.

```py
newTuple = prevTuple[:]
newString = prevString[:]
```

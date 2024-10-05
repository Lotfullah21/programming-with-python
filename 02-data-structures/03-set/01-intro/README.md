## Empty set

Empty set can be created using `set()` keyword.

```py
s0 = set()
print(type(s0))

s0 = {}
print(s0)
```

## Distinct

Elements in a set should be distinct, when we try to add duplicate elements, set will remove them and only keeps distinct ones.

```py
s1 = set([10,10])
print(s1) // {10}

s2 = {10,10}
print(s2) // {10}
```

## Using set

when using `set()` function, we cannot pass a single integer, whatever we pass, it should be a collection of items, being `tuples,list,dict`

```py
# set(1) value error
```

## creating set from collections

- 1. list

```py
slist = set([1,2,3,4,2,1])
print("set of list", slist)


```

- 2. tuple

```py
stuple = set((1,2,3,4,2,1,"hello","ahmad"))
print("set of tuple", slist)

sdict = set({1:"1","a":"ahmad",2:"3",2:"9"})
print(sdict)
```

- 3. dictionary

```py
sdict = set({1:"1","a":"ahmad",2:"3",2:"9"})
print(sdict)
```

By default, it will consider only the keys, but if we want to have keys,values or combination `key-val`, we have to pass the methods to get those specific items.
For instance, to get the keys, we use `dict.keys()`, to get the values, we use `dict.values()` and to get both, we use `dict.items()`.

## Note:

- Sets do not allow duplicate keys at any cost
- When keys are the same, the last duplicate key will over write the previous duplicate key
- When doing operations with a dictionary using key, always remember that the set consider only the unique keys.

```py
dict1 = {1:"1","a":"ahmad",2:"3",2:"9"}
sdict2 = set(dict1.values())
print(sdict2) # Output: {a, ahmad, 9}

sdict3 = set(dict1.keys())
print(sdict3) # Output: {1, a, 2}

sdict4 = set(dict1.items())
print(sdict4) # Output: {(1, '1'), (2, '9'), ('a', 'ahmad')}


```

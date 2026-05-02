## set comprehension

We can create sets from a list of items using list comprehension.

```py
l = [1,2,3,4,5,6,7,8]
newSet = {x for x in l}
print(newSet)
```

## dictionary comprehension

For dictionary comprehension, we need to have key and values.

```py
l = [1,2,3,4,5,7,8,10]
d = {x:x**2 for x in l}
print(d) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 7: 49, 8: 64, 10: 100}
```

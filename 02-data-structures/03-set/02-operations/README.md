## 1. Insertion

```py
s = {1,2}
print(s) # {1,2}
s.add(12)

```

Adding an element that is already present does not change the set.

```py
s = {1,2}
s.add(1)
print(s) # {1,2}
```

#### update(collection)

A collection of items can be passed as an argument to the `update` method to be added to the set.

```py
s.update(["a",1,4,0])
print(s) # {0, 1, 2, 4, 12, 'a'}
s.update(("a",1,4,1,-1))
print(s) # {0, 1, 2, 4, 12, 'a', -1}
```

```py
s.update(("a",1,4,1,-1), ["apple","phone"])
print(s)
```

## 2. Removal

We have `remove()`, `discard()` and clear methods to be used for removal in sets.

- 1. discard

It removes the given argument from the set, if the item is not present, it does not raise an error.

```py
s = {1,2, 3}
s.discard(1) # Output: {2,3}
print(s)
s.discard(4)
print(s) # Output: {2,3}
```

- 2. remove

It is same as discard, but it will raise key error if the item is not present.
To be on the safe side, first check if the item is present, if not return or show an understandable message to the end user.

```py
s = {1, 2, 3}
s.remove(1) # Output: {2,3}
print(s)
s.remove(4) # KeyError 4
```

- 3. clear

It clears our set, but the set object is still present in our memory and items can be added later.

```py
s = {1,2, 3}
s.clear()
print(s) # set()
```

- 4. del

It removes the entire object from the memory and items cannot be added later.

```py
s = {1,2, 3}
del s
print(s) # name 's' is not defined
```

## len

It returns number of items present in list.

```py
s = {1,2, 3}
print(len(s)) # 3
```

## in

It checks whether a given element is present or not.

```py
s = {1,2, 3}
print(1 in s) # True
print(10 in s) # False
```

## Operations on two sets

#### union (s1|s2)

It combines and returns distinct elements of two sets.

```py
s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}
s3 = s1.union(s2)
print(s3) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

Union also can be achieved using,`|` symbol as well.
`s1|s2`

#### Intersection (s1&s2)

It returns the common elements of two sets.

```py
s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}
s4 = s1.intersection(s2)
print(s4) # {1, 3}
```

Intersection of two sets also can be found using `&` symbol.

```py
s4 = s1&s2
print(s4) # {1, 3}
```

#### Difference (s1-s2)

It returns a new list which are not present in other set.

```py
s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}
# Return a set which are in `s1`, but not in `s2`.
s4 = s1.difference(s2)
print(s4) # Output: {2, 4, 5}
```

Intersection of two sets also can be found using `-` symbol.

```py
s4 = s1-s2
print(s4) # Output: {2, 4, 5}
```

#### Symmetric difference (s1^x2)

It returns a new set with elements that are present in both sets, but not the common ones.

```py
s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}
s4 = s1.symmetric_difference(s2)
print(s4) # Output: {2, 4, 5, 6, 7, 8}
```

Symmetric difference of two sets also can be achieved using `^` symbol.

```py
s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}
s4 = s1^s2
print(s4)
```

## Boolean operation

#### isdisjoint

It returns a boolean value.
If there is no common element between the sets, it returns `True`, if there is a common element, it returns `True`.

```py
s5 = s1.isdisjoint(s2)
print(s5)
```

#### issubset (s1<=s2)

A set is said to be subset of other set if all of its elements are present in the other set.
It returns True if an element is subset of the other element.

```py
s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}
s4 = s1.issubset(s2)
print(s4) # False
```

```py
s1 = {1,2}
s2 = {1,2,3}
s4 = s1.issubset(s2)
print(s4) # True
```

`issubsetset` also can be checked using `<=` symbol as well.

#### proper subset

If s1 is subset of s2 and length of s2 is bigger than s1, then we can say s1 is proper subset of s2.

```py
s1 = {1,2}
s2 = {1,2,3}
s4 = s1<s2
print(s4)
```

#### Superset

If all elements of s2 is present in s1, then we say s1 is superset of s2.

```py
s1 = {1,2}
s2 = {1,2,3}
s4 = s1.issuperset(s2)
print(s4) ## False
```

`issuperset` also can be checked using `>` symbol as well.

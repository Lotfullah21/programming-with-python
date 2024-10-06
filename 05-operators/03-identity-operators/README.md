## Identity operators

## 1. is

In Cpython implementation of python, id is the address of the objects in the memory.

It checks for the `ids` of two values, if the ids are the same, that means they are stored at the same memory location and their values are the same, hence it returns `True`.
On the other hand, if ids are the same, it will return `False`.

```py
a = 10
b = 10
print(a is b) # True

x = 10
y = -10
print(x is y) # False
```

## 2. is not

It checks for opposite, if `ids` are not the same, it returns `True` and if `ids` are different, it returns `False`

```py
a = 10
b = 10
x = 10
y = -10
print(x is not y) # True
print(a is not b) # False
print (None is None) # True
```

## For collections

In case of collection containers like list and tuples, even if the values are the same, it will not return `True`, because even if the value of objects are the same, they will be stored at different locations.

```py
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)
```

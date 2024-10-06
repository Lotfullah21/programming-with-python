## Range

It is a function provided by python, it returns a list of integers

### 1. range(x)

It returns a list of numbers starting from `0` up to `x`, but `x` is not included.

```py
x = range(5)
print(x) # range(0, 5)
print(type(x))  # <class 'range'>
```

range is a different type from other data types like `tuple, list, ... set`, but it is considered a sequent type.

We can use `list` constructor to get a list of numbers.

```py
x = range(5)
print(list(x)). # [0, 1, 2, 3, 4]
```

### 2. range(start,end)

It generates a sequence `[start+1, start+2, start+2,...,end-1]`

```py
x = range(1, 5)
print(list(x)). # [1, 2, 3, 4]
```

```py
x = range(-2, 2)
print(list(x)). # [-2,-1,0,1]
```

### 3. range(start, end, increment-value)

By default, the increment value is 1, but we can add that argument as well.

```py
x = range(1, 5, 2)
print(list(x)). # [1, 3]
```

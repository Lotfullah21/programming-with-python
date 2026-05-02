# Global Variables

A global variable is created outside a function. A function can read it directly.

```python
x = 2

def show_x():
    print(x)

show_x()
```

## Local Variables

A local variable is created inside a function and belongs to that function.

```python
def total():
    a = 12
    b = 12
    print(a + b)
```

`a` and `b` cannot be used outside `total`.

## Changing A Global Variable

To assign a new value to a global variable inside a function, use `global`.

```python
count = 2

def increment_count():
    global count
    count = count + 1

increment_count()
print(count)  # 3
```

Use global variables carefully. Functions are usually easier to test when they receive values as parameters and return results.

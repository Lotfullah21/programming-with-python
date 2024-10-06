## else

It should be followed by an `if` block and if the expression inside `if` evaluated to false, the code inside `else` block will be executed.

```py
a = 10
if (a>1):
    print(f"{a} is greater than 1")
else:
    print(f"{a} is smaller than 1")
```

## Crucial

A flow will start from the last `if` before `else`. If we have multiple `if` blocks before last `if` before `else`, those blocks does not affect our code.

```py
a = 10
if (1==1):
    print("a==1")
if (a>1):
    print(f"{a} is greater than 1")
else:
    print(f"{a} is smaller than 1")
```

Now, the output will be `1==1` and `10 is greater than 1`

## elif

It creates a flow where if the first `if` expression evaluates to `False`, the code inside `elif` block will get executed.

```py
a = 10
if (a>11):
    print(f"{a} is greater than 11")
elif (a>10):
    print(f"{a} is greater than 10")
elif (a>9):
    print(f"{a} is great than 9")
else:
    print(f"{a} is smaller than 10")
```

The if-elif-else block evaluates conditions one by one in order, and as soon as one condition is True, it executes the corresponding block and skips the rest.

#### Another approach, but wrong one

```py
if (a>11):
    print(f"{a} is greater than 11")
if (a>10):
    print(f"{a} is greater than 10")
if (a>9):
    print(f"{a} is great than 9")
else:
    print(f"{a} is smaller than 10")
```

Here, each if statement is independent. It evaluates all conditions one by one, regardless of whether a previous condition was true.

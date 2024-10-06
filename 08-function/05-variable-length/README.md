### 3. Variable length argument

#### 1. non-keyword arguments

We can define functions that accept any number of arguments using \*args (for non-keyword arguments) and \*\*kwargs (for keyword arguments).

We can pass a variable number of arguments using a special symbol `*`.
It collects all the elements inside a tuple.

- `*arg(No keyword required)`: Collects extra arguments as a tuple

```py
t=0
def sum(*arg):
    for i in arg:
        t+=i
    print(t)
sum(1,2,3,4,6)
```

#### 2. keyword arguments

- `**kwargs(Keyword arguments shall be passed)`: Collects extra keyword arguments as a dictionary.

```py
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="ahmad", age=25)
# Output:
# name: ahmad
# age: 25
```

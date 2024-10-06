## Create a function

```py
def FUNCTION_NAME(PARAMETERS):
    STATEMENT
```

### def

`def` is a reserved keyword which is used to create a function.

### Function name

to name a function, we should follow some rules

- name cannot start with integers
- name cannot be an integer
- name should be descriptive of the function

Among the given functions, which one is more descriptive?

```py
def a(a,b):
    print(a+b)
```

```py
def total(a, b):
    print(a+b)
```

### parameters

Theses are the values that our function is going to work with or we can pass to the function.

### Calling a function

to use a function we must call it and to call a function, we use `function-name(parameters)`

```py
total(2,3)#5
```

We can call function as many time as want.

```py
def total(a,b):
    print(a+b)
print("Hello world")
total(2,3)
print("Greeting from library")
total(3,5)
```

Function can have no inputs as well.

```py
def greeting():
    print("Hello world")

greeting() # Hello world
```

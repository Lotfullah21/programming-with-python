## Function

a reusable block of code

A function is a set of statements that take inputs, do some specific computation and produce output.

The idea is that to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

The main idea behind the function is write the code once and use it as many times as you want.

[GFG](https://www.geeksforgeeks.org/batch/python-foundation-sp-april/track/Python-Foundation-Functions/article/NjczOQ%3D%3D)

## Application of functions

- avoid code redundancy
- make the code modular, divide into chunks
- easy to maintain
- easy to read
- avoid variable collisions, variables are not connected across functions
- Functions create local scope, which means variables defined inside a function are local to that function and don’t interfere with variables outside

```py
def function_a():
    x = 10  # Local to function_a
    print(f"x in function_a: {x}")

def function_b():
    x = 20  # Local to function_b
    print(f"x in function_b: {x}")

x = 30  # Global scope
function_a()  # Output: 10
function_b()  # Output: 20
print(f"x globally: {x}")  # Output: 30

```

## Creating a function

A function can be created using `def` keyword.

```py
def FUNCTION_NAME(PARAMETER1, PARAMETER2):
    STATEMENT1
    STATEMENT2
    STATEMENT3
```

## Parameter

Parameters are placeholders defined in the function definition that receive input values when the function is called.

## Arguments

Arguments are the actual values passed into the function when it’s called.

## Types of argument

### 1. Default Argument

Functions can have default values for parameters. If the caller doesn’t pass an argument, the function uses the default value.

```py
def greet(name="ahmad"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, ahmad!
greet("ali")  # Output: Hello, ali!

```

### 3. Variable length argument

#### 1. non-keyword arguments

We can define functions that accept any number of arguments using \*args (for non-keyword arguments) and \*\*kwargs (for keyword arguments).

We can pass a variable number of arguments using a special symbol `*`.

- `*arg(No keyword required)`: Collects extra arguments as a tuple

```py
t=0
def sum(*arg):
    for i in arg:
        t+=i
    print(t)
sum(1,2,3,4,6)
```

#### 2. key-word arguments

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

## Docstring

The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function. The use of docstring in functions is optional but it is considered a good practice.

```py
def evenOdd(x):
    """Function to check if the number is even or odd"""

    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(evenOdd.__doc__)
```

## function return value

`return` is a statement that ends the execution of a function and return a value(if provided) to the caller of the function.
The statements after `return` is not executed.

If the return statement is without any expression, then the special value None is returned.

```py

def add(a, b):
    return a + b
total = add(2,1)
print(total)#3
```

## Lambda Functions (Anonymous Functions)

```py
square = lambda x: x * x
print(square(5))  # Output: 25

```

## Variables as references:

In Python, a variable does not directly store a value like in some other languages (e.g., C, where variables store memory addresses or values).
Instead, a variable holds a reference (or pointer) to an object in memory.
Multiple variables can point to the same object.

## Passing variables to functions:

When you pass a variable to a function, you're passing the reference to the object it points to, not a copy of the object itself.
This means that if the function modifies the object, the change will be reflected outside the function, if the object is mutable (e.g., lists, dictionaries).

Mutable objects (like lists, dictionaries, sets, etc.) can be modified in place, so changes made to them inside a function will persist outside the function.
Immutable objects (like integers, strings, tuples, etc.) cannot be modified in place. Any operation that seems to "change" the object actually creates a new object, leaving the original one unchanged.

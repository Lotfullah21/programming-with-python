## global variable

- these are variables that are created outside functions or `class`.
- they are accessible from any where in our code.

```py
x = 12
name = "ahmad"
def total():
    a = 12
    b = 12
    print(a+b)
```

`name` and `x` are global variables.
`a and b` are local variables.

We can access to global variables insider our function and use its value.

```py
x=2
def fun():
    w = x +  1
    print(x)
fun()
print(x)
```

To change a global variable inside a function, we need to pass `global var-name` inside the function.

```py
x=2
def fun():
    global x
    x = x +  1
    print(x)
fun()
print(x)
```

## local variables

- these are variables defined within a function
- they are local to that function
- cannot be accessed outside of that function

```py
def total():
    a = 12
    b = 12
    print(a+b)
```

`a and b` are local variables.

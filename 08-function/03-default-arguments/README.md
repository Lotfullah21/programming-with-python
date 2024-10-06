## Default arguments

We can have predefined values for our function, if the user does not provide any value for that argument, function will use the default argument.
If the user provides a value instead of default argument, the default argument will be overwritten.

```py
def greeting(greet,name="ahmad"):
    print(greet, name)

greeting("salam")
print("hello", "king")
```

### Note

Once, default arguments passed to a function, python expects from us that we pass the default arguments after that, other wise it raises an error.

```py
def greeting(greet,name="ahmad", age):
    print(greet, name)
```

`age` have been passed after default argument `name`, not acceptable for python, it raises the following error : `SyntaxError: parameter without a default follows parameter with a default`.

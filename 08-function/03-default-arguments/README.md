# Default Arguments

A default argument gives a parameter a value to use when the caller does not provide one.

```python
def greeting(greet, name="Ahmad"):
    print(greet, name)

greeting("Salam")        # Salam Ahmad
greeting("Hello", "Ali") # Hello Ali
```

## Rule

Parameters with defaults must come after parameters without defaults.

This works:

```python
def greeting(greet, name="Ahmad", age=20):
    print(greet, name, age)
```

This does not work:

```python
def greeting(greet, name="Ahmad", age):
    print(greet, name, age)
```

Python raises `SyntaxError: parameter without a default follows parameter with a default`.

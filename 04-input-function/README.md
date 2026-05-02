# Input

`input()` asks the user to type something and press Enter.

By default, input is always a string.

```python
name = input("Enter your name: ")
print("Hello", name)
```

If the user does not provide an input, the rest of the code will not get executed.

## Summation With User Input

Convert input to `int` before doing arithmetic.

```python
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("sum =", x + y)
```

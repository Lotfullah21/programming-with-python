## 1. s.rstip("char")

`rstrip` is used to remove unwanted characters from right side of a string

```py
s = "----Hello world, Hello india---+"
# it removes + char from right hand side of a string.
s1 = s.strip("+")
print(s) # ----Hello world, Hello india---+
print(s1) # ----Hello world, Hello india---
```

## 2. s.lstrip("char")

It removes the unwanted characters from left side of a string

```py
s = "----Hello world, Hello india"
s1 = s.lstrip("-")
print(s) #  ----Hello world, Hello india---
print(s1) #  Hello world, Hello india
```

## s.strop("char")

It removes unwanted characters from both side of a string.

```py
s = "----Hello world, Hello india---+++++"
s1 = s.strip("+-")
print(s)  # ----Hello world, Hello india---+++++
print(s1) # Hello world, Hello india

```

By default, if no parameter is passed, these methods will remove whitespace characters.

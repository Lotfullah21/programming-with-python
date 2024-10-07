## Formatted string

Mainly, there are three ways to write formatted strings in python.

### 1. using %

```py
greeting = "hello"
name="ahmad"
s = "%s %s welcome to india"%(greeting, name)
print(s)
# hello ahmad welcome to india
```

### 2. using format function

```py
sf = "{0} {1} welcome to india".format(greeting, name)
print(sf)
# hello ahmad welcome to india
```

### 3. using f-string

It one of the most used method

```py
fs = f"{greeting} {name} welcome to india"
print(fs)
# hello ahmad welcome to india
```

we can use expression inside f-string

```py
a =12
b =10
print(f"{a}+{b}={a+b}")
# 12+10=22
```

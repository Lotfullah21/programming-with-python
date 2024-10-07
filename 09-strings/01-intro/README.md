## string

strings are immutable, once created, they cannot be changed.

```py
greeting = "Hello"
greeting[0]="A" # Error, cannot assign to a string.
```

## Triple quote string

Using """ """, we can create a multi line string.

```py
greeting = """ Hello Ahmad
Welcome to hooshmandlab,
you will enjoy here.
"""


```

## \n

When we use `\n`, we are adding a new line to our string.

```py
newline = "Hello world\nwelcome to india"
print(newline)
# Hello world
# welcome to india
```

## escape and raw sequence

When we try to write a path to a file, most probably, we use `\` and sometimes they are combined with characters that makes them escape character.
for instance, adding them with `\n`, it will create a new line.

```py
s1= "C:\project\name.py"
print(s1)
#Output:  C:\project
# ame.py
```

To make a string to treat every character as a raw character, we add `r` before our string.

```py
s1= r"C:\project\name.py"
print(s1)
# C:\project\name.py
```

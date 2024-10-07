## String operations

### 1. substring

A substring is a sequence of characters that appears in the same order within another string. If a string A contains another string B as a part of it, then B is called a substring of A.
All the consecutive sequence of characters/character or sub string of a string.
empty string and the whole string is also considered as substring.
Using `in` operator, we can check for substrings.

```py
s1 = "helloworld"
s2 = ""
s4 = "helworld"

print(f"{s2} in {s1}: {s2 in s1}")
print(f"{s4} in {s1}: {s4 in s1}")
```

`s4 = "helworld"`, it might look that it is present in s1, indeed it is present, but `in` looks for consecutive characters.

### 2. concatenation

when one string is appended to the end of another string, it is called concatenation.
we can perform this operation by adding `+` between two strings.

```py
s1 = "Hello"
s2 = " World"
s3 = s1 + s2
print(s3)
```

### 3. position

`s1.index(s2)` checks and returns the index of s2 in s1.

```py
s1 = "Hello World"
s2 = "World"
print(s1.index(s2))

```

if substring is not present, it raises value error.

### 4. len()

It returns the count of total elements present in the string.
Empty spaces are also counted as an element when using `len()`

```py
s1 = "Hello World"
print(len(s1)) # 11
```

### 5. s.lower()

It converts our string to upper case

```py
s1 = "Hello World"
print(s1.lower())  # hello world
```

### 6. s.islower()

It returns True if all characters of a string are in lower case.

### 7. s.upper()

It converts our string to lower case

```py
s1 = "Hello World"
print(s1.upper())  # HELLO WORLD
```

### 8. s.isupper()

It returns True if all characters of a string are in upper case.

# 09. Strings

A string is an ordered sequence of characters. Strings are immutable, which means you cannot change a character in place after the string is created.

```python
word = "Python"
print(word[0])   # P
print(word[-1])  # n
```

## Lessons

| Lesson | Folder | Main idea |
| --- | --- | --- |
| 1 | [01-intro](01-intro/README.md) | Create strings and use escapes |
| 2 | [02-formatted-string](02-formatted-string/README.md) | Insert values into strings |
| 3 | [03-operations](03-operations/README.md) | Concatenate, slice, index, and convert |
| 4 | [04-comparison](04-comparison/README.md) | Compare strings |
| 5 | [04-methods](04-methods) | Use common string methods |
| 6 | [05-searching](05-searching/README.md) | Search inside strings |
| 7 | [06-palindrome](06-palindrome/README.md) | Check whether text reads the same backward |
| 8 | [07-reverse](07-reverse/README.md) | Reverse strings |
| 9 | [08-decimal-to-binary](08-decimal-to-binary/README.md) | Convert decimal text to binary |
| 10 | [09-binary-to-decimal](09-binary-to-decimal/README.md) | Convert binary text to decimal |

## Immutability

This does not work:

```python
word = "Python"
word[0] = "J"  # TypeError
```

Create a new string instead:

```python
word = "Python"
word = "J" + word[1:]
print(word)  # Jython
```

## Characters And Codes

Use `ord` to get a character code and `chr` to convert a code back to a character.

```python
print(ord("A"))  # 65
print(chr(65))   # A
```

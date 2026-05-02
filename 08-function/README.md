# 08. Functions

A function is a named, reusable block of code. Functions make programs easier to read, test, and reuse.

## Lessons

| Lesson | Folder | Main idea |
| --- | --- | --- |
| 1 | [01-intro](01-intro/README.md) | Define and call a function |
| 2 | [02-how-function-works](02-how-function-works/README.md) | Understand call flow |
| 3 | [03-default-arguments](03-default-arguments/README.md) | Provide default parameter values |
| 4 | [04-positional-vs-keyword-args](04-positional-vs-keyword-args/README.md) | Pass arguments by position or name |
| 5 | [05-variable-length](05-variable-length/README.md) | Use `*args` and `**kwargs` |
| 6 | [06-global-variables](06-global-variables/README.md) | Understand global and local scope |
| 7 | [07-returning-values](07-returning-values/README.md) | Send results back with `return` |
| 8 | [08-parameter-passing](08-parameter-passing/README.md) | See how mutable and immutable values behave |
| 9 | [09-problems](09-problems) | Practice function problems |

## Basic Pattern

```python
def add(a, b):
    return a + b

total = add(2, 3)
print(total)  # 5
```

## Why Functions Matter

- They remove repeated code.
- They give a task a clear name.
- They create local scope, so variables inside one function do not collide with variables in another.
- They make code easier to test because each function can be checked separately.

## Parameters And Arguments

Parameters are the names in the function definition. Arguments are the values passed during the function call.

```python
def greet(name):      # name is a parameter
    print("Hello", name)

greet("Ahmad")        # "Ahmad" is an argument
```

## while loop

Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.

Syntax:

```py
while CONDITIONAL_TEST:
    STATEMENT1
    STATEMENT2
    STATEMENT3
```

While loop falls under the category of indefinite iteration. Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance.
Python uses indentation as its method of grouping statements. When a while loop is executed, expression is first evaluated in a Boolean context and if it is true, the loop body is executed. Then the expression is checked again, if it is still true then the body is executed again and this continues until the expression becomes false.

[GFG](https://www.geeksforgeeks.org/batch/python-foundation-sp-april/track/Python-Foundation-Loops/article/NjcyMw%3D%3D)

```py
i = 0
while i<5:
    print(i)
    i = i+1
```

It is extremely crucial to look how you are going to end or exit from the loop, the test condition should be in such a way that there has to be a variable that controls it inside the while loop and we have ot make sure that it eventually will become `False`, otherwise, we enter into an `infinite` loop.

Explanation:
Initialization:

- i starts at 0.

Loop Condition:

- The loop continues as long as i < 5.
  Iteration Process:

- In each iteration:
  The current value of i is printed.

```table

### Evaluation of `i`:

| Iteration | Value of `i` | Output   |
|-----------|---------------|----------|
| 1         | 0             | 0        |
| 2         | 1             | 1        |
| 3         | 2             | 2        |
| 4         | 3             | 3        |
| 5         | 4             | 4        |
| 6         | 5             | - (exit) |

```

For instance, in the following snippet, if we do not add to `i` a value in each iteration, it is obvious that `0<5` and it will run infinitely.

```py
i = 0
while i<5:
    print(i)
```

Explanation:
Initialization:

i starts at 0.
Loop Condition:

The loop continues as long as i < 5.
Iteration Process:

In each iteration:
The current value of i is printed.
There is no change to i, which means it remains 0.

```table

### Evaluation of `i`:

| Iteration | Value of `i` | Output   |
|-----------|---------------|----------|
| 1         | 0             | 0        |
| 2         | 0             | 0        |
| 3         | 0             | 0        |
| ...       | 0             | ...      |

```

Instead of adding to `i`, we are decrementing from it and it causes an infinite loop.

```py
i = 0
while i<5:
    print(i)
    i=i-1
```

```table
### Evaluation of `i`:

| Iteration | Value of `i` | Output   |
|-----------|---------------|----------|
| 1         | 0             | 0        |
| 2         | -1            | -1       |
| 3         | -2            | -2       |
| ...       | -3            | -3       |

```

## Infinite Loop

An **infinite loop** is a loop that continues to execute indefinitely because the terminating condition is never met. One common way to create an infinite loop in Python is by using `while True`.

## Example of an Infinite Loop

The following example demonstrates an infinite loop using `while True`:

```python
while True:
    print("This loop will run forever!")
```

To make a while True loop functional and avoid it running forever, we can include a condition inside the loop that allows you to break out of it

```py
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
# 0 1 2
```

In Python, the else block associated with a while loop is executed only if the loop completes normally, meaning it doesn't hit a break statement

## How the else block works with loops:

The else block in a loop is executed only if the loop is not terminated by a break statement.
If the loop completes all iterations naturally (without encountering a break), the else block runs.
If the loop is interrupted by a break, the else block is skipped.

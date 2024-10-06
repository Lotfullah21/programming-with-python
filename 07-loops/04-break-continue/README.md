## 1. break

We use `break` to exit the loop immediately as soon as a certain condition is met. Once `break` is encountered, the control flow jumps out of the loop, and the next line of code after the loop (if any) is executed.

### Example:

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
```

```text
0
1
2
3
4

```

## 2. continue

We use continue to skip the rest of the code inside the loop for the current iteration and move to the next iteration. It does not terminate the loop but just skips to the next iteration.
Or simply, when the condition is meet, do not execute the statements after `continue` statement.

```py
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the even numbers
    print(i)

```

```text
1
3
5
7
9

```

For instance, if we have a database of items to be sold and its related information.
If for some item we have missing values, we can use `continue` to skip the calculations for those items.

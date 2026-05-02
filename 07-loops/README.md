# 07. Loops

Loops repeat a block of code. They are useful when you need to process many values or keep going until a condition changes.

## Lessons

| Lesson | Folder | Main idea |
| --- | --- | --- |
| 1 | [01-while-loop](01-while-loop/README.md) | Repeat while a condition is true |
| 2 | [02-range](02-range/README.md) | Generate integer sequences |
| 3 | [03-for-loop](03-for-loop/README.md) | Loop over ranges and collections |
| 4 | [04-break-continue](04-break-continue/README.md) | Exit or skip part of a loop |
| 5 | [05-nested-loops](05-nested-loops/README.md) | Put one loop inside another |
| 6 | [06-patterns](06-patterns/README.md) | Print shapes with loops |
| 7 | [07-math-problems](07-math-problems) | Practice with digits, factorial, and GCD |

## `while` Or `for`

Use `while` when you do not know how many times the loop will run.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Use `for` when you are looping over a known sequence.

```python
for number in range(5):
    print(number)
```

Python does not have a built-in `do while` loop. If you need that behavior, write a `while True` loop and use `break` when the stopping condition is met.

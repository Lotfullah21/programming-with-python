# 06. Control Flow

Control flow lets a program choose which lines to run.

## Lessons

| Lesson | Folder | Main idea |
| --- | --- | --- |
| 1 | [01-if](01-if/README.md) | Run a block only when a condition is true |
| 2 | [02-if-else](02-if-else/README.md) | Choose between two or more branches |
| 3 | [03-problems](03-problems/README.md) | Practice decisions with numbers and dates |

## Basic Pattern

```python
temperature = 32

if temperature > 30:
    print("Hot day")
else:
    print("Not too hot")
```

## Blocks

Python uses indentation to mark a block of code. All statements inside the same block must line up.

```python
if True:
    print("inside the block")
    print("also inside")

print("outside the block")
```

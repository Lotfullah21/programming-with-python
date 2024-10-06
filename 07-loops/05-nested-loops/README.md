## Nested Loops in Python

A nested loop is a loop inside another loop

The outer loop runs a certain number of times, and for each iteration of the outer loop, the inner loop runs completely.

```py
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # Code block for inner loop
    # Code block for outer loop

```

```py
# Nested for loop example
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} * {j} = {i * j}")
    print("---")

```

Things to Keep in Mind:
Efficiency: Nested loops can lead to inefficient code if not used carefully, especially if both loops run many iterations.
Loop Control: break and continue can be used to control nested loops. For example, break can exit the inner loop, while continue can skip iterations in either the inner or outer loop based on conditions.

```py
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break  # Exit the inner loop
        print(f"{i}, {j}")

```

## Applications of nested loops

## Use Cases of Nested Loops

1. ### Working with 2D Arrays or Matrices:

   You can use nested loops to traverse through rows and columns of a 2D list (or matrix).

   ### Example:

   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]

   for row in matrix:
       for element in row:
           print(element, end=" ")
       print()  # Move to the next line after each row
   ```

2. ### Generating Combinations:

Nested loops are helpful for generating combinations of elements from multiple lists

```py
colors = ["red", "blue"]
shapes = ["circle", "square"]

for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")

```

### 3.Drawing Patterns:

Nested loops are commonly used to print patterns like triangles, squares, or grids.

```py
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()  # Newline after each row
```

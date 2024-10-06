## Control Flow

Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a program. We can control the flow of execution by using conditional statements, loops, and other constructs to determine which specific block of code should be executed based on certain conditions.

### Block

A **block** is a piece of code that is grouped together and treated as a single unit. It has its own environment or scope and is typically indented to visually distinguish it from the surrounding code. In Python, blocks of code are defined by their indentation.

Example of a block within a control structure:

```python
a = 5
if a > 3:
    # This is a block of code
    print("a is greater than 3")
    b = a + 2
    print(f"b is now {b}")
```

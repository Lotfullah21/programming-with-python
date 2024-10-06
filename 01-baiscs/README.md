## What is a Statement?

A statement is an instruction that performs some action. It represents a complete command to be executed, but it does not necessarily return a value.

A statement can be a combination of expressions.
Typically, statements control the flow of execution in a program (e.g., if, for, while).
Example of a Statement:

```py
x = 5 # Assignment statement
if x > 3: # Conditional statement
print("x is greater than 3") # Print statement
```

In the above example:

- `x = 5` is a statement that assigns the value 5 to x.
- `if x > 3`: is a conditional statement.
- `print("x is greater than 3")` is also a statement that outputs text.

## What is an Expression?

An expression is any valid combination of variables, constants, operators, and functions that produces a value. Expressions always return a result when evaluated.

Expressions are part of statements.
The value of an expression can be used in other expressions or statements.
Example of an Expression:

```py
y = 2 + 3 # Expression: 2 + 3
z = y _ 4 # Expression: y _ 4
```

In this example:

- `2 + 3` is an expression that evaluates to 5.
- `y \* 4` is another expression that evaluates based on the value of y.

#### Statement vs Expression

```table

| Statement                                      | Expression                              |
|------------------------------------------------|----------------------------------------------|
| Performs an action or command.                | Produces or returns a value.                |
| Can contain one or more expressions.          | Can be part of a statement.                  |
| Does not necessarily return a value.          | Always evaluates to a value.                |
| Example: `x = 10` (assignment).               | Example: `5 + 2` (evaluates to 7).          |

```

An expression evaluates to a value but does not perform an action on its own.
A statement performs an action and may contain expressions within it.

`a = 3 + 3` is both a statement and contains an expression.

`Expression`:

3 + 3 is an expression. It combines the constants 3 and 3 using the addition operator, which evaluates to 6.

`Statement`:

The entire line a = 3 + 3 is a statement because it performs the action of assigning the value of the expression (6) to the variable a.

## for loop

It is used to iterate through a sequence.
a sequence can be `string`,`list`,`tuple`

A sequence is an essential data structure in programming that represents an ordered collection of elements. Understanding how to work with sequences is fundamental to manipulating and organizing data efficiently.

Syntax:

```py
for x in sequence:
    STATEMENT1
    STATEMENT2
    STATEMENT3
```

Iteration through a list

```py
for x in [1,2,3,4]:
    print(x,end="") # 1234
```

Iteration through a string

```py
for x in "course":
    print(x, end=" ") # c o u r s e
```

Whatever statement we write inside a loop, that will be executed for each single item in the sequence we are iterating through.

```py
for x in range(5):
    print(x, end=" ") # 0 1 2 3 4

```

We can use indices to access to the list values.

```py
x = [1,2,2,3,4,5]
for i in range(len(x)):
    print(x[i])
```

the above approach gives us the position of the element as well.

## Table

```py

a = 5
for i in range(1,11):
    print(f"{i}*{a} = {i*a}")

1*5 = 5
2*5 = 10
3*5 = 15
4*5 = 20
5*5 = 25
6*5 = 30
7*5 = 35
8*5 = 40
9*5 = 45
10*5 = 50
```

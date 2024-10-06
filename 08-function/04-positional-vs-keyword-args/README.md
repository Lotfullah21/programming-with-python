## Positional arguments

When we pass the arguments exactly matching their place holder in parameters, they are called positional arguments.
order is important here

```py
def printDetails(name, age, place):
    print(f"{name} is {age} years old and lives in {place}")
printDetails("ahmad", 26, "hyderabad")
```

## Keyword arguments

When we pass the arguments along their place holder names, they are called keyword arguments. because we are adding the names, order does not matter here.

```py
def printDetails(name, age, place):
    print(f"{name} is {age} years old and lives in {place}")
printDetails(age=26, place="India", name="King")
```

```py
def fun(x):
    x = 10
x = 12
fun(x)
print(x)
```

Initially both of the x's are referencing to the same value, 12, But after executing the code inside the function, now local x refers to value 10 and global x refers to value 12.

## Local scope

- All the variables inside a function is local to that variable and cannot be accessed from outside
- All the variables outside the functions are global
- we cannot change the global variables unless we use `global` keyword inside the function.

```py
x=2
def fun():
    x = x +  1
    print(x)
fun()
print(x)
```

It will throw the following error: `cannot access local variable 'x' where it is not associated with a value`.

To change a global variable, we use `global var-name` inside the function.

```py
x= 2
def fun():
    global x
    x = x +  1
    print(x)
fun()
print(x)
```

## collections

In the following code, we are not adding a new list, we are just changing the value of a mutable object, hence both local and global lists are referencing the same object and any change inside the function will be reflect to the `global list`.

```py
def fun(l):
    l.append(12)
l =[1,2,3,4]
fun(l) # [1, 2, 3, 4, 12]
print(l) # [1, 2, 3, 4, 12]

```

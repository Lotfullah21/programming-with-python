a = 10; b=100
print("a =", a)
print("b =", b)

# Now, lets swap them, remember to store the memory address of the variables before swapping
temp = a
a = b
b = temp
print("After swapping the values: ")
print("a =", a)
print("b =", b)
print("\n")
# Swapping also can be done using `,` separated values

x = 10
y = 20
print("x =", x)
print("y =", y)
x, y = y, x
print("After swapping the values: ")
print("x =", x)
print("y =", y)
# We can assign multiple variables as well.
x, y = y+12, x-10
print("x =", x)
print("y =", y)
def operations(x, y):
    total = x + y
    sub = x - y
    div = x//y
    return total, sub, div


total, sub, div  = operations(12, 12)
x = operations(12,12)
print(x)
print("total =",x[0])
print("diff =",x[1])
print("div =",x[2])
print(total, sub, div)
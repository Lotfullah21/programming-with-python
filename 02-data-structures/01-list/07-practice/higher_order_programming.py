def applyToEach(L1, fn):
    for i in range(len(L1)):
        L1[i] = fn(L1[i])
    return L1


def fact(ele):
    factorial = 1
    if ele < 0:
        return "None"
    elif ele <= 1:
        return 1
    else:
        for i in range(1, ele+1):
            factorial = factorial * i
    return factorial


L1 = [5.8, 2.0, 3, -4]

print("absolute =", applyToEach(L1, abs))
print("integer =", applyToEach(L1, int))
print("factorial =", applyToEach(L1, fact))


def applyFunctions(fn, L):
    for f in fn:
        print(f(L))


print(applyFunctions([abs, int, fact], 3))

mapped = map(abs, L1)

for e in map(abs, L1):
    print(e)

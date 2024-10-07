def decToBin(n):
    if n==0:
        return "0"
    res = ""
    while n>0:
        res = res + str(n%2)
        n=n//2
    return res[::-1]

n = int(input("Enter an integer: "))
res = decToBin(n)
print(res, type(res))


def decToBin(n):
    res = bin(n)
    return res

n = int(input("Enter an integer: "))
res = decToBin(n)
print(res, type(res))

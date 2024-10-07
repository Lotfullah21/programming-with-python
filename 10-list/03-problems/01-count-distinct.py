def countDistinct(n):
    res = 0
    for i in range(len(n)):
        # checking upto i, if there is a similar element.
        if n[i] not in n[0:i]:
            res+=1
    return res
l = [1,2,2,4,5,3,1]
print(countDistinct(l))

# Using set
def countDistinct(n):
    s = set(n)
    return len(s)
l = [1,2,2,4,5,3,1]
print(countDistinct(l))
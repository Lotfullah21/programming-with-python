def binToDecimal(b):
    rs = b[::-1]
    res = 0
    p = 0
    for ele in rs:
        res = res + int(ele)*(2**p)
        p+=1
    return res
        
n = input("Enter a binary number: ")
res = binToDecimal(n)
print(res)

def binToDec(b):
    return int(b, 2)


print(binToDec(n))
a = int(input("Enter a number: "))


def getFirstDigit(a):
    while a>=10:
        a=a//10
    print(a)

getFirstDigit(a)
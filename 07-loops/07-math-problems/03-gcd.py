a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

limit = min(a, b)
gcd = 1

for value in range(1, limit + 1):
    if a % value == 0 and b % value == 0:
        gcd = value

print(gcd)

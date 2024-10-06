a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

min = min(a, b)
gcd = 1
for i in range(1, min+1):
    if a%i==0 and b%i==0:
        gcd = i


print(gcd)
        
        
        
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

largest = float("-inf")
if a>=b and a>=c:
    largest = a
elif c>=a and c>=b:
    largest = c
else:
    largest = b
    
    
print(f"largest of {a,b,c} is", largest)

print(max(a,b,c))
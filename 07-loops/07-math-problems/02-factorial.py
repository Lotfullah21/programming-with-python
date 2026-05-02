number = int(input("Enter a number: "))
total = 1

for value in range(1, number + 1):
    total = total * value

print("factorial =", total)

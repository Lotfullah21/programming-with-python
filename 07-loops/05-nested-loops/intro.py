# Nested for loop example
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} * {j} = {i * j}")
    print("---")


i = 1
while i <= 3:  # Outer loop
    j = 1
    while j <= 3:  # Inner loop
        print(f"{i}, {j}")
        j += 1
    i += 1

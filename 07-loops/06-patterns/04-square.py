def print_hollow_square(s):
    for i in range(s):
        for j in range(s):
            # Print '*' for borders, otherwise print space
            if i == 0 or i == s - 1 or j == 0 or j == s - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # Newline after each row

# Example usage:
s = 4  # Input size of the square
print_hollow_square(s)

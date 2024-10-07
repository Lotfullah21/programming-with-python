def alphabets(c1, c2):
    # Generate the range of characters from c1 to c2 using ord() and chr()
    for ch in range(ord(c1), ord(c2) + 1):
        print(chr(ch), end=' ')  # Print the character without adding a newline


print("geeksforgeeks".endswith("geeks",1,13))
print(len("geeksforgeeks"))
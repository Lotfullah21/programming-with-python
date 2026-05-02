# remove empty spaces
text = input("Enter a string: ").replace(" ", "").lower()

low = 0
high = len(text) - 1
while high >= low:
    print(text[high], end="")
    high -= 1
print()


# second method
rev = ""
for ele in text:
    # add the new element at the beginning of a string.
    rev = ele + rev

print(rev)

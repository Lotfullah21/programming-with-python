# remove empty spaces
text = input("Enter a string: ").replace(" ", "").lower()

l = 0
h = len(text)-1
while h>=l:
    print(text[h],end="")
    h-=1
print()


# second method
rev = ""
for ele in text:
    # add the new element at the beginning of a string.
    rev = ele + rev
    
print(rev)
    
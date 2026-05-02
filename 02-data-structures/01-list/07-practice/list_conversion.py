# We can convert a list to a string using list(string)

greeting = "hello"
print("string", greeting)
print("list", list(greeting))

# string -> list: we can use join methods

L1 = ["Salam", "Hello", "1", "10"]
print("\n------Join method-------\n")
S1 = "".join(L1)
print("string S1", S1)
S2 = " ".join(L1)
print("stringS2", S2)
S3 = "_".join(L1)
print("string S3", S3)

# using split method to split a string based on some specification and returns a list. it only works on strings
print("\n-----Split method-----\n")
L2 = S2.split("1")
print("List L2", L2)

L3 = S3.split("Hello")
print("List L3", L3)

L4 = S2.split(" ")
print("List L4", L4)

# Sorting a list
# Sorted will give us a new list without changing the original list
unsorted_l = [10, 121, 22, 3, 41, 5, 6]
sorted_l = sorted(unsorted_l)
print("Unsorted list", unsorted_l, "\nSorted list", sorted_l)

# list.sort() will mutate the original list

us = [0, 12, 1, 3, 1, 2, 3]
us.sort()
print("sorted list", us)

reversed = us.reverse()
print("Reversed list", us)

for i in range(5, 3, -1):
    print(i, type(i))

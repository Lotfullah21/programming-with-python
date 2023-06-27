# concatenation

L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4]
L3 = L1 + L2
print("L3", L3)
print("append method", L2.append(30))
# returns the reomved element,means remove the ele at index 1
print("Pop at specific index", L2.pop(1))
print("L2 = ", L2)
print("Remove", L2.remove(1))
print(L2)
print("Pop method =", L2.pop())
# add an element to the end of a list

L1.append(100)
print("L1", L1)

# extend a list by adding a list to the end of the original list
L2.extend(["Hello", "Salam", "Bonjur", "hi"])

# delete an element with a specific index
print("L2", L2)
del (L2[4])
print("sL2", L2)

# delete a specific element with list.remove(ele), if multiple elemenst of the target is there
# remove the first occurence
L2.remove("hi")
print("L2", L2)

# Remove the element from the of a list
L1.pop()
print("L1", L1)

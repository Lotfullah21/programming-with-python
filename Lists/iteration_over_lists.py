L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

summation = 0
for i in range(len(L)):
    summation = summation + L[i]
print(summation)

# iterarating over a list meansn directly iterating over the elements in the list
total = 0
# go to the L, and take each value
for j in L:
    # add values to the total
    total += j

print(total)

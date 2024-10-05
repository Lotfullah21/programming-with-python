s1 = {1,2,3,4,5}
s2 = {1,3,6,7,8}

s3 = s1.union(s2)
print(s3)
print(s1|s2)

s4 = s1.intersection(s2)
print(s4)
s4 = s1&s2
print(s4)


s4 = s1.difference(s2)
print(s4)

s4 = s1-s2
print(s4)

s4 = s1.symmetric_difference(s2)
print(s4)
s4 = s1^s2
print(s4)

s5 = s1.isdisjoint(s2)
print(s5)

s4 = s1.issubset(s2)
print(s4)

s1 = {1,2}
s2 = {1,2,3}
s4 = s1<s2
print(s4)


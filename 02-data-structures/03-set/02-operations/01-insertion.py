s = {1,2}
print(s)
s.add(12)
print("after insertion",s)
s.add(1)
print(s)


s.update(["a",1,4,0])
print(s)
s.update(("a",1,4,1,-1))
print(s)
s.update(("a",1,4,1,-1), ["apple","phone"])
print(s)
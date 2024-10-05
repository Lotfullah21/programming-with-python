s0 = set()
print(type(s0))

s0 = {}
print(s0)


s1 = set([10,10])
print(s1)

s2 = {10,10}
print(s2)

slist = set([1,2,3,4,2,1])
print("set of list", slist)

stuple = set((1,2,3,4,2,1,"hello","ahmad"))
print("set of tuple", slist)

sdict = set({1:"1","a":"ahmad",2:"3",2:"9"})
print(sdict)


dict1 = {1:"1","a":"ahmad",2:"3",2:"9"}
sdict2 = set(dict1.values())
print(sdict2)

sdict3 = set(dict1.keys())
print(sdict3)

sdict4 = set(dict1.items())
print(sdict4)
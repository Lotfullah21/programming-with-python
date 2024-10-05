d = {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
print(d.get("name"))
print(d.get("age"))
print(d.get("city"))
print(d.get("city","city is not present in the dictionary"))

print(len(d))
d.pop("name")
print(d)



d = {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
d["city"] = "Musqat"
print(d)
d.popitem()
print(d)
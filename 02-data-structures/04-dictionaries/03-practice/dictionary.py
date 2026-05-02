student = {"name": "Lotfullah", "age": 25, "school": "Internet", 1: 1}
print(student)
# indexing using keys
print(student["name"])

# adding an element to the dictionary
student["field"] = "Artificial Intelligence"
print(student)

# delete an element
del (student["age"])
print(student)

# checking using in
print("name" in student)
print("Interest" in student)
print(25 in student)

# get the keys
print("Keys ", student.keys())
# get the values, keys() and values() methods, both of them returns an iterable
print("Values", student.values())

# dictionary.items() iterates over key and values

for i, j in student.items():
    print("key", i, "value", j)

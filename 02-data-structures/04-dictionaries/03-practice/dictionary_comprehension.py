# comprehension is a powerful way to create data structures,such as lists,dictionaries and sets.
# <variable> = { key:new_value for (key, value) in <dictionary>.items() }
student = {"name": "Lotfullah", "age": 25, "school": "Internet", 1: 1}

new_dict = {key for key in student.keys()}
new_dict_value = {val for val in student.values() if val == "lotfullah"}
print(new_dict_value)

new_dict_value = {
    key: val + " Andishmand" for (key, val) in student.items() if val == "Lotfullah"}
print(new_dict_value)


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    a = aDict.values()
    return len(a)


print(how_many(student))


# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.

#     returns: int, how many values are in the dictionary.
#     '''
#     # Your Code Here
#     suma = 0
#     for val in aDict.values():
#         suma += len(val)
#     return suma


# print(how_many(student))

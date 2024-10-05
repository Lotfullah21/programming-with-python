## Dictionary

An empty dictionary can be created using `{}`.

## Creating a dictionary

The value of a dictionary can be access using its key and by referencing that key, it can be updated as well.

We can create a dictionary using pre defined values

```py
numbers = {1:"1",2:"2",3:"3"}
print(numbers) # {1: '1', 2: '2', 3: '3'}

mixedDict = {1:"1","abc":"abc",False:True}
print(mixedDict)
```

A dictionary also can be created first by creating an empty dictionary and later on adding the values by specifying the keys.

```py
newDict = {}
newDict["name"] = "ahmad"
newDict["age"] = 21
newDict["place"] = "Jordan"
print(newDict). # {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
```

## Updating a dictionary

We can update the value of a dictionary by using `dictionaryName[key]=new-value`.

```py
numbers = {1:"1",2:"2",3:"3"}
print(numbers) # {1: '1', 2: '2', 3: '3'}

numbers[1]=100
print(numbers) # {1: 100, 2: '2', 3: '3'}
print(numbers[3]) # "3"
```

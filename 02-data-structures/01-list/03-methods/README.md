## Methods

methods are functions that are particular to a specific kind of a object and can be applied to that object only.

Python, provides variety of methods to be used with list.

#### 1. append

It allows us to add an element to the end of a list.

#### 2. extend

We can extend our original list by passing collection of items.

```py
# Create a collection of apples
fruits = ["apple","banana","grapes","orange"]
print(fruits)
fruits.extend([2, 32])
print(fruits)
fruits.extend((2, 32))
print(fruits)
```

The items we pass should be wrapped inside a collection of elements which are iterable.

#### 3. insert

Syntax

```py
list.insert(at which index to be inserted, element)
```

```py
fruits.insert(1, "Hello")
print(fruits)
```

#### 4. pop

remove an element from the end of the list and return that element

```py
last_item = my_list.pop()
print(last_item) # Output: 6
print(my_list) # Output: [1, 2, 3, 4, 5]
```

We can add the index to the pop function as well and it will remove the element at that index.

```py
last_item = my_list.pop(3)
print(last_item) # Output: 4
print(my_list) # Output: [1, 2, 3, 5]

```

#### 5. del

It is a general purpose keyword that can be we used with other collections as well.

```py
del[index of the element to be removed]
del[starting index: ending index] // delete all element starting from the given index excluding the end index.
```

```py

# Inserts an element at specified index
fruits = ["apple","banana","grapes","orange"]
print(fruits)
# Insert `Hello` at index 1.
del fruits[1]
print(fruits)
del fruits[0:2]
print(fruits)
```

### Additional methods

```py
# 4. remove: remove this element, if the item is not present, it raises value error.
my_list.remove('a')
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]



# 6. clear, clear the list
my_list.clear()
print(my_list)  # Output: []

# 7. index: return the index of given element
my_list = [1, 2, 3, 2, 1]
print(my_list.index(2))  # Output: 1

# 8. count: count the occurrence of given element.
print(my_list.count(2))  # Output: 2

# 9. sort: sort the list
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 2, 3]

# 10. reverse: reverse the list
my_list.reverse()
print(my_list)  # Output: [3, 2, 2, 1, 1]

# 11. copy: create a copy of original list
new_list = my_list.copy()
print(new_list)  # Output: [3, 2, 2, 1, 1]
```

## Note

Some of the methods only works for specific kind of data, for instance

- `list.sum()` will not work if the elements are non-numeric type
- `list.min()` will not work if we are having mixed data types like `numerics` and `non-numerics`, same goes for `max()` method.
- `list.sort()` will not work if we are having mixed kind of data, it needs to compare the elements.

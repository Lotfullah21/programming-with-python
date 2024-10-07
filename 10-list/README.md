## list

The list is a sequence data type which is used to store the collection of data. Tuples and String are other types of sequence data types.

## Creating a list

Lists in Python can be created by just placing the sequence inside the square brackets[]. Unlike Sets, a list doesn’t need a built-in function for the creation of a list.

```py
l1 = []
print(type(l1))  # <class 'list'>

l2 = ["a","b","c"]
print(l2) # ['a', 'b', 'c']
```

## Accessing elements from the List

In order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing.

```py
print(l2[0]) # a
print(l2[1]) # b
```

## Negative indexing

negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.

```py
print(l2[-1]) # c
print(l2[-2]) # b
```

## Getting the size of the Python list

Python len() is used to get the length of the list, size means how many elements are present inside a list.

```py
# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))
```

## Adding Elements to a Python List

Elements can be added to the List by using the built-in append() function. Only one element at a time can be added to the list by using the append() method, for the addition of multiple elements with the append() method, loops are used. Tuples can also be added to the list with the use of the append method because tuples are immutable. Unlike Sets, Lists can also be added to the existing list with the use of the append() method.

```py
# Adding elements
l2.append(2)
l2.append(3)
l2.append((-1,-2,-3))
print(l2) # ['a', 'b', 'c', 2, 3, (-1, -2, -3)]
l2.append({"a":"1","b":"2"})
print(l2) # ['a', 'b', 'c', 2, 3, (-1, -2, -3), {'a': '1', 'b': '2'}]
```

## reversed

The reversed() function does not return a new collection; instead, it returns an iterator that yields the elements of the iterable in reverse order.

```py
my_list = [1, 2, 3, 4]
rev_list = reversed(my_list)

# You can convert the iterator back to a list
print(list(rev_list))  # Output: [4, 3, 2, 1]
```

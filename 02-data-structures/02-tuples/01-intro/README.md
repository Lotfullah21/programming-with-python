Tuples also can be created with separated commas in between.
For instance, `10, 12, 129` is a tuple, also `10,` is a tuple.

Tuples are faster than lists.
We use them in scenarios where the values are not going to changes or there is a fixed range of values.
For instance,

- Days of the week
- Gender
- Admin roles

Most of the list operation is supported by tuples, like indexing, count, len and index.
Functionalities that modify the lists are not available, like sort, reverse and clear.

tuples are immutable in Python, we cannot append elements to a tuple directly. However, we can achieve a similar effect by creating a new tuple that combines the original tuple with the new elements.

## 1. concatenation

```py
my_tuple = (1, 2, 3)
new_element = (4,)  # A single element tuple, note the comma
my_tuple = my_tuple + new_element  # Concatenation
print(my_tuple)  # Output: (1, 2, 3, 4)

```

## 2. Method 2: Convert to List and Append, then Convert Back to Tuple

```py
my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # Convert tuple to list
my_list.append(4)  # Append the new element
my_tuple = tuple(my_list)  # Convert back to tuple
print(my_tuple)  # Output: (1, 2, 3, 4)

```

## 3. Method 3: Using += (Syntactic Sugar for Concatenation)

```py
my_tuple = (1, 2, 3)
my_tuple += (4,)  # Add new element
print(my_tuple)  # Output: (1, 2, 3, 4)

```

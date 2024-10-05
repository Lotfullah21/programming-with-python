# 1. Iterable:

An iterable is any Python object that can return its elements one at a time, allowing us to loop over it using a for loop.

### Key Feature:

It must implement the `__iter__()` method, which returns an iterator. An iterator can then be used to get elements one at a time using the`__next__()` method until the end of the collection is reached.

Examples of Iterables:

- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Generators
- Files

In short, all sequences are iterables, but not all iterables are sequences. For example, sets and dictionaries are iterables but not sequences.

### Key methods

` __iter__()`

# 2. Sequence:

A sequence is a specific type of iterable that supports indexing and ordering. In other words, elements in a sequence have a specific order, and you can access elements by their position (index) in the sequence.

### Key Features:

- Order is important: The elements have a well-defined order.
- Supports indexing and slicing: You can access elements using their index (e.g., sequence[0]).
- Supports iteration: You can loop through sequences as they are also iterables.

Examples of Sequences:

- Strings ("hello")
- Lists ([1, 2, 3, 4])
- Tuples ((1, 2, 3))

These objects allow you to access elements using indexes, which is not always possible with all iterables.

### Key methods

`__iter__()`, `__getitem__()`,`__len__()`

# Objects

everything in python are objects, and each object has

1. data
2. operations
3. functions and methods to play with the object.

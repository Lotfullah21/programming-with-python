## List []

list is an ordered sequence of data, where its size can be changed as data related to a particular list changes.

it is an ordered sequence of object types.
it is also called dynamic array.

## main points

1. lists are mutable, which imply that the element inside a list can be changed.
2. mostly, lists contains same kind of data, like strings or integers.
3. it can also contain mixed kind of data.

## Without list

Let's create a scenario where we need to store different kinds of fruits, if we create and assign values to each individual fruit name a fruit, it looks redundant and cumbersome.

```py
apple = "apple"
banana = "banana"
grapes = "grapes"
orange = "orange"
print(apple, banana, grapes, orange)
```

## How to create a list

lists can be created using `[]`, when python interpreter counters the `[]`, it infers that it is a list.

Now, having the inspiration from the above problem, let's solve it using a list.

```py
# Create a collection of apples
fruits = ["apple","banana","grapes","orange"]
```

# Indexing

Python lists are stored in contiguous memory blocks,it means that the list elements are arranged one after the other in a continuous sequence of memory addresses. The memory for the entire list is allocated in a single, continuous block, rather than being scattered throughout different parts of memory.

## Memory in a Computer:

Memory in a computer is essentially a large, numbered collection of slots (addresses) where data can be stored.
When a Python list is created, the system allocates a continuous chunk of memory to hold all the references (pointers) to the objects in the list. Each element of the list is stored at a specific memory address, and these addresses are next to each other (contiguous) in memory.

## What Contiguous Memory Means:

In a contiguous block of memory, each element's memory address follows directly after the previous one. If element A is stored at memory address X, and each reference takes up k bytes of space, then the next element B will be stored at address X + k, and so on
for the rest of the elements in the list.

#### Example

```py
newList = [10, 20, 30, 40]

```

```table

| List Index | Element | Memory Address | Value |
|------------|---------|----------------|-------|
| 0          | 10      | 1000           | 10    |
| 1          | 20      | 1004           | 20    |
| 2          | 30      | 1008           | 30    |
| 3          | 40      | 1012           | 40    |
```

Here:

- Element 10 is stored at address 1000,
- Element 20 is stored at address 1004,
- Element 30 is stored at address 1008,
- Element 40 is stored at address 1012.

what is actually stored at a memory address like 1008 is not the value itself (in this case, 30), but rather a reference (or pointer) to the object that holds that value. Here’s a breakdown of how this works

The list myList contains references to these integer objects. So, if we consider the memory addresses, we might have something like:

- At address 1000: reference to the integer 10 (let's say it points to address 1500)
- At address 1004: reference to the integer 20 (points to address 1600)
- At address 1008: reference to the integer 30 (points to address 2000)
- At address 1012: reference to the integer 40 (points to address 1700)

## How it works:

#### Base Address:

Python knows the base address of the list (e.g., 1000).

#### Index Calculation:

#### For myList[2], it calculates:

Memory Address = Base Address + (Index × Size of Each Reference)
Memory Address = 1000 + (2 × 4) = 1008

#### Retrieve Reference:

At address 1008, it finds a reference (pointer) to the actual integer object 30, which is stored at another memory address (e.g., 2000).

#### Access the Value:

Python follows this reference to access the integer value 30.

## List Object Metadata:

A Python list is an object in memory that not only stores the actual elements (or references to elements) but also contains metadata.

#### This metadata includes information such as:

The length of the list.
The capacity of the allocated memory (since Python lists are dynamic and can grow).
The base address of the allocated memory block (where the first element is stored).

## Benefits of Contiguous Memory in Lists:

### Fast Indexing:

Because elements are stored in contiguous memory, Python can quickly calculate the memory address of any element using a simple formula:
Memory Address of Element at Index i = BASE ADDRESS + (i \* SIZE OF ELEMENT)

For example, if you want to access the element at index 2 (newList[2]), Python calculates the address by starting from the base address (1000 in the example above) and moving 2 positions forward (1000 + 2 \times 4 = 1008), so it knows that newList[2] is stored at memory address 1008.

### Cache Friendliness:

Since the elements are stored together in memory, modern CPUs can take advantage of cache mechanisms. When the CPU fetches an element, it often pulls in neighboring elements into the cache, which speeds up access when iterating over the list

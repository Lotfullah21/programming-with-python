# initialize a tuple
myTuple = ()
print(type(myTuple),myTuple)

# When there is a single element, add a `,` at the end, otherwise it will be treated as single integer
tuple_n = (12)
print("no comma for single int",type(tuple_n)) # integer

tuple_1 = (12,)  # tuple
print(type(tuple_1))


tuple_str = ("hello")
print("no comma for single string",type(tuple_str)) # string

tuple_str = ("hello",)
print("adding comma",type(tuple_str)) # tuple



tuple_1 = (1, 2, 3)
print("tuple_1 =",tuple_1)

tuple_mixed = (1,2,"hello","salam")
print("tuple mixed =",tuple_mixed)

print(tuple_1[0])
print(tuple_1[1])

# Concatenation
tuple_concatenate = tuple_1 + tuple_mixed
print("tuple_concatenate =",tuple_concatenate)

# error, we cannot mutate tuples
# tuple_concatenate[0] = 10 //  error
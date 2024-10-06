### Explicit

Here, we have specify from which data type to which data type, we want our data to be converted.

```py
a = 10
print(10)
print(float(10))
```

```py
a = 10
b = 12.2
sum= a+b
print(sum) # 22.2
print(int(sum)) # 22
print(str(sum)) # 22.2
```

`string` to `int`

```py
a = "12"
b = 10
sum = int(a)+b
print(sum)
```

Sometimes, its not possible to convert one type to another, for instance converting a string of alphabets to an integer.

`string` to `in` with char base

```py
a = "ab"
b = 10
sum = int(a)+b
print(sum)
```

#### Collection conversion

List to other collections

```py
a = [1,2,3,4,5,6,6,1]
print(tuple(a)) # (1, 2, 3, 4, 5, 6, 6, 1)
print(set(a)) # {1, 2, 3, 4, 5, 6}
```

We cannot convert the above collection to dictionary.

String to other collections

```py
a = "hooshmandlab"
print(list(a)) # ['h', 'o', 'o', 's', 'h', 'm', 'a', 'n', 'd', 'l', 'a', 'b']
print(tuple(a)) # ('h', 'o', 'o', 's', 'h', 'm', 'a', 'n', 'd', 'l', 'a', 'b')
print(set(a)) # {'a', 'b', 'l', 'd', 'n', 'o', 's', 'm', 'h'}
```

### Integer to binary, hexadecimal and octal

```py
num = 8
print(bin(num)) # 0b1000
print(hex(num)) # 0x8
print(oct(num)) # 0o10
```

`0b1000`, the prefix `ob` tells us that it is not a normal integer, it is a binary.

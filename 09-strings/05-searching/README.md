## s.find("word to be searched")

It returns the starting index of `item` we are searching for, if the item is not present unlike `index` method, it does not raise value error, but rather it returns -1.

```py
s = "Hello world, Hello india"
print(s.find("Hello")) # 0
print(s.find("ina")) # -1
print(s.index("hello")) #  ValueError: substring not found

```

One thing to look here is, theses methods are case sensitive.

```py
print(s.find("Hello")) # 0
print(s.find("hello")) #  -1
```

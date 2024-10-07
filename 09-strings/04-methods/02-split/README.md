## 1. s.split(params)

It splits our string into a list of word based on a parameter.
If parameter is a ",", the string will be separated based on those params.
If no parameter is added, by default, the params will be empty spaces in a string.

```py
s = "Hello world, Hello india"
newS = s.split()
print(newS) # ['Hello', 'world,', 'Hello', 'india']
```

split based on a "-"

```py
s1  =  "Hello-world-welcome-to-india"
print(s1.split("-")) # ['Hello', 'world', 'welcome', 'to', 'india']
```

## 2. "".join(s)

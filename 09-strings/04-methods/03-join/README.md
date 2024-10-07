## 2. "param".join(s)

It joins a list of items with the `params` being placed between each item.
We can say that it converts a list into a string.

```py
l = ['Hello', 'world', 'welcome', 'to', 'india']
s = "".join(l)
print(s) # Helloworldwelcometoindia
```

```py
l = ['Hello', 'world', 'welcome', 'to', 'india']
s = " ".join(l)
print(s) # Hello world welcome to india
```

```py
l = ['Hello', 'world', 'welcome', 'to', 'india']
s = "-".join(l)
print(s) # Hello-world-welcome-to-india
```

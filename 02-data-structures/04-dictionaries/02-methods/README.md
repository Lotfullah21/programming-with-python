## Methods

A dictionary like other collections comes with in-built methods.

#### d.get(key)

It returns to us the values associated to the given key.
If the key is not present, it returns `None`.

```py

d = {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
print(d.get("name")) # ahmad
print(d.get("age")) # 21
print(d.get("city")) # None
```

If use `[]`, if the key is not present, it raises `ket` error.

```py
print(d["city"]) # KeyError: 'city'
```

So, we have to use `if-else` conditional to avoid the error

```py
if "city" in d:
    print(d["city"])
else:
    print("city","city is not present in the dictionary")
```

Now, a shortcut using `get` method would to pass a custom message as second parameter if the key is not present to the `get` method.

```py
print(d.get("city","city is not present in the dictionary"))  # city is not present in the dictionary
```

## len()

It gives the number of `key-value` pairs.

```py
print(len(d))  # 3
```

## pop(key)

It removes the `key-value` pair corresponding to the key passed to the function.

```py
d = {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
print(d.pop("name")) # {'age': 21, 'place': 'Jordan'}
```

## del d[key]

It deletes the `key-value` corresponding to the key and does not return any thing.

```py
d = {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
del d["name"]
```

## d.popitem()

It removes the last inserted `key-val` pair

```py
d = {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
d["city"] = "Musqat"
print(d) # {'name': 'ahmad', 'age': 21, 'place': 'Jordan', 'city': 'Musqat'}
d.popitem()
print(d) # {'name': 'ahmad', 'age': 21, 'place': 'Jordan'}
```

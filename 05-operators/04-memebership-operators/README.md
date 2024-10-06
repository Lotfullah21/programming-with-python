## in

using `in` operator, we can check whether the given element is present in another container or not.
For each different container, we look for different membership, for instance,

- `string`: checks for substring
- `dictionary`: checks for key
- `list, tuple, set` checks for membership

It returns a boolean value

```py

x = 10
l1 = [1,2,3,4,10,20]
print(x in l1) # True

a = "doctor"
l2 = "doctor from Tanzania"
print(a in l2) # True


```

## not in

It is opposite of `in`, it checks if the given element is not in the other container.

```py
l2 = "doctor from Tanzania"
print("Beatus" not in l2) # True
```

## comparison

Strings are compared character by character and under the hood, their `ASCII` values are compared to each other.

For instance `ASCII(a)<ASCII(c)`.

```py

s1 = "hello"
s2 = "world and universe"
print(s1>s2)
print(s1==s2)
print(s1!=s2)
print(s1<s2)
```

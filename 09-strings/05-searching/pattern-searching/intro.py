text = "Hello world"
pattern= "hello"
pos = text.lower().find(pattern)
# The moment we don't find the pattern, the position becomes -1.
while pos>=0:
    print(pos)
    # find the given patter starting from given position
    pos = text.lower().find(pattern, pos+1)
    
    
    

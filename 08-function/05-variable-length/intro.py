# non-keyword arguments
def printArgs(*args):
    print(args)
printArgs(1, "2", "a", "2")



# Keyword arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="ahmad", age=25, place="hyderabad")

# Now, id becomes mandatory.
def printDetailsWithId(id, **kwargs):
    print(f"details with id {id}: ")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
        
printDetailsWithId(10, name="milad", place="Hyderabad")
x = 2


def read_global():
    print("inside:", x)


read_global()
print("outside:", x)


count = 2


def increment_count():
    global count
    count = count + 1
    print("inside after increment:", count)


increment_count()
print("outside after increment:", count)

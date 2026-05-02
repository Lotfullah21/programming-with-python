number = int(input("Enter a number: "))


def get_first_digit(value):
    value = abs(value)
    while value >= 10:
        value = value // 10
    return value


print(get_first_digit(number))

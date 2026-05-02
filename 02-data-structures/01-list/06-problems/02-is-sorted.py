def is_sorted(numbers):
    i = 1
    while i < len(numbers):
        if numbers[i] < numbers[i - 1]:
            return False
        i += 1
    return True


values = [1, 2, 2, 4, 5, 3, 1]
print(is_sorted(values))

def count_distinct_slow(values):
    count = 0
    for index in range(len(values)):
        if values[index] not in values[:index]:
            count += 1
    return count


def count_distinct(values):
    return len(set(values))


numbers = [1, 2, 2, 4, 5, 3, 1]
print(count_distinct_slow(numbers))
print(count_distinct(numbers))

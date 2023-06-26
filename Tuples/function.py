# defining the function
def minMax(nums):
    minimum = min(nums)
    maximum = max(nums)
    # using tuples, we can return more than one value.
    return (minimum, maximum)


# calling the function
min, max = minMax([12, 32, 32, 0, -1])
print("min", min, "maximum", max)

def add(a, b):
    return  a + b


def subtract(a, b):
    return a - b


def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

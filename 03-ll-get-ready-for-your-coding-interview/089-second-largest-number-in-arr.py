"""
Find the second-largest number in an array.
"""


def second_largest(arr):
    largest_number = None
    second_largest_number = None

    for i in arr:
        if largest_number is None:
            largest_number = i
        elif i > largest_number:
            second_largest_number = largest_number
            largest_number = i
        elif second_largest_number is None:
            second_largest_number = i
        elif i > second_largest_number:
            second_largest_number = i

    return second_largest_number


numbers = [1, 3, 4, 5, 0, 2]
numbers2 = [-2, -1]
numbers3 = [2, 2, 1]
numbers4 = [2]
numbers5 = []

print(second_largest(numbers))
print(second_largest(numbers2))
print(second_largest(numbers3))
print(second_largest(numbers4))
print(second_largest(numbers5))


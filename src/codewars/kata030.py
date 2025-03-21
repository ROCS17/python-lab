"""
Beginner - Reduce but Grow

Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""


def grow(arr):
    aux = 1
    for i in arr:
        aux *= i

    return aux


print(grow([1, 2, 3, 4]))

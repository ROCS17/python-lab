"""
Square(n) Sum

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9
"""

from functools import reduce


def square_sum(numbers: list):
    return reduce(lambda x, y: x + y**2, numbers, 0)


print(square_sum([1, 2, 2]))

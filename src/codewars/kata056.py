"""
8 kyu - Sum Mixed Array

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
"""


def sum_mix(arr: list):
    return sum([int(element) for element in arr])


print(sum_mix([9, 3, "7", "3"]))

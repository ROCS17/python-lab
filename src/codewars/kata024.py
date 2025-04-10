"""
8 kyu - Sum of positive

Task
You get an array of numbers, return the sum of all of the positives ones.

Example
[1, -4, 7, 12] =>  1 + 7 + 12 = 20

Note
If there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr: list):
    return sum([i for i in arr if i > 0]) if arr else 0


print(positive_sum([1, -4, 7, 12]))

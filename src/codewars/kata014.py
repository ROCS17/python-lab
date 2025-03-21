"""
Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]
"""

from typing import List


def maps(a: List[int]) -> List[int]:
    return list(map(lambda x: x * 2, a))


print(maps([1, 2, 3]))

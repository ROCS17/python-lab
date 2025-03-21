"""
Sort the odd

Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

from typing import List


def sort_array(source_array: List[int]) -> List[int]:
    source_array_aux = sorted([i for i in source_array if i % 2 != 0])
    for index, value in enumerate(source_array):
        if value % 2 != 0:
            source_array[index] = source_array_aux.pop(0)
    return source_array


def sort_array_solution(source_array: List[int]) -> List[int]:
    source_array_aux = sorted([i for i in source_array if i % 2 != 0])
    return [x if x % 2 == 0 else source_array_aux.pop(0) for x in source_array]


def other_solution(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    print(odds)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


# print(sort_array([5, 8, 6, 3, 4]))
print(sort_array_solution([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

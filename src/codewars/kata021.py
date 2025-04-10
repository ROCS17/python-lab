"""
6 kyu - Array.diff

Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].
If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
"""


def array_diff(a: list, b: list):
    match (a, b):
        case ([], _):
            return []
        case (_, []):
            return a
        case (_, _):
            for i in b:
                if i in a:
                    for k in range(a.count(i)):
                        a.remove(i)
            return a


def other_solution(a, b):
    return [x for x in a if x not in b]


print(array_diff([1, 2, 2], []))

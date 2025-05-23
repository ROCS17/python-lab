"""
5 kyu - Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst: list):
    count_number_zero = lst.count(0)
    list_aux = [i for i in lst if i != 0]
    for i in range(0, count_number_zero):
        list_aux.append(0)
    return list_aux


def another_solution(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

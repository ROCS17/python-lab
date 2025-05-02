"""
7 kyu - Mumbling

This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(st: str):
    list_st = list(st)

    list_mumbling = [
        char.upper() + (char.lower() * index) for index, char in enumerate(list_st)
    ]
    return "-".join(list_mumbling)


print(accum("cwAt"))

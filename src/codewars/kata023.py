"""
Beginner Series #2 Clock

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000

Input constraints:
0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
"""


def past(h, m, s):

    return (
        h * 3600000 + m * 60000 + s * 1000
        if (0 <= h <= 230) and (0 <= m <= 59) and (0 <= s <= 59)
        else 0
    )


print(past(0, 1, 1))

"""
8 kyu - Quarter of the year

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
and month 11 (November), is part of the fourth quarter.

Constraint:
1 <= month <= 12
"""


def quarter_of(month: int):
    match month:
        case 1 | 2 | 3:
            return 1
        case 4 | 5 | 6:
            return 2
        case 7 | 8 | 9:
            return 3
        case 10 | 11 | 12:
            return 4
        case _:
            return 0


print(quarter_of(12))

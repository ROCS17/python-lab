"""
8 kyu - Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""


def bool_to_word(boolean: bool):
    return "Yes" if boolean else "No"


print(bool_to_word(True))

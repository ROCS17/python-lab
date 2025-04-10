"""
8 kyu - Remove exclamation marks

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.


"""


def remove_exclamation_marks(s: str):
    return s.replace("!", "")


print(remove_exclamation_marks("Hellow World!"))

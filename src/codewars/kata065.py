"""
7 kyu - Get the Middle Character

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
- If the string's length is odd, return the middle character.
- If the string's length is even, return the middle 2 characters.

Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
"""


def get_middle(s: str):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1 : len(s) // 2 + 1]


print(get_middle("test"))

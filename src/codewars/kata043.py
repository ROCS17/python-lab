"""
8 kyu - Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""


def double_char(s: str):
    word = ""
    for i in s:
        word += i * 2
    return word


print(double_char("Hello"))

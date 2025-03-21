"""
Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
Return the resulting string.

Note: input will never be an empty string
"""


def fake_bin(str_number: str):
    return "".join(["0" if int(number) < 5 else "1" for number in list(str_number)])


print(fake_bin("012345"))

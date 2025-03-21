"""
Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence: str):
    counter = 0
    for char in "aeiou":
        counter += sentence.count(char)
    return counter


print(get_count("aeiou"))

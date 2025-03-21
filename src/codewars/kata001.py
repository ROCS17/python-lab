"""
Descending Order
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in
descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321
"""


def descending_order(num):
    num_desc = ""
    aux = list(str(num))
    aux.sort(reverse=True)
    for value in aux:
        num_desc = num_desc + value
    return int(num_desc)


# Solution
def descending_orders(num):
    return int("".join(sorted(str(num))))


print(descending_order(1201))
print(descending_orders(1201))

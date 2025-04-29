"""
6 kyu - The Supermarket Queue

There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required for all the customers to check out!


input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

output
The function should return an integer, the total time required.

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
"""


def queue_time(customers, n):
    if not customers:
        return 0

    if n >= len(customers):
        return max(customers)

    cajas = [0] * n

    for cliente in customers:
        cajas[cajas.index(min(cajas))] += cliente

    return max(cajas)

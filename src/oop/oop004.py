"""
1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius**2)

    def perimeter(self):
        return 2 * pi * self.radius


circle = Circle(5)
print(circle.area())
print(circle.perimeter())

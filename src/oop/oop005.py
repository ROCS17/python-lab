"""
2. Write a Python program to create a person class. Include attributes like name, country and date of birth.
Implement a method to determine the person's age.
"""

from datetime import datetime


class Person:
    def __init__(self, name, country, date_birth):
        self.name = name
        self.country = country
        self.date_birth = date_birth
        self.date_birth = date_birth
        self.date_birth = date_birth

    def age(self):
        return datetime.now().year - self.date_birth


person = Person("Roger", "Lima-Peru", 2000)

print(person.age())

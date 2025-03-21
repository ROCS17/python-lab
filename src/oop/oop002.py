"""
Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un
metodo 'cumpleaños', que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con 'Persona'.
Tendríamos que lograr ejecutar el siguiente código con la clase creada:

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


person = Person("Roger", 25)
print(person.age)
person.birthday()
print(person.age)

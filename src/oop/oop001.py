"""
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota
y si ha aprobado o no.
"""


class Student:
    def __init__(self, name, calification):
        self.name = name
        self.calification = calification

    def __str__(self):
        if self.calification < 11:
            return f"Nombre: {self.name} con calificación {self.calification}. Usted ha desaprobado"
        else:
            return f"Nombre: {self.name} con calificación {self.calification}. Usted ha aprobado"


student = Student("Roger", 20)
print(student.__str__())

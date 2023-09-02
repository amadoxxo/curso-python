# 1. Ejemplo de Herencia en Python
# 2. Sobreescritura del metodo __str()__ en Python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona[Nombre: {self.nombre} Edad: {self.edad}]'

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def __str__(self):
        return f'Empleado[Salario: {self.salario}] {super().__str__()}'


# empleado1 = Empleado('Elian', 21, 5000)
# print(empleado1.nombre)
# print(empleado1.edad)
# print(empleado1.salario)
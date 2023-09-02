# 1. Clases y Objetos en Python

class Persona:
    pass

print(type(Persona))


# 2. Clases y Objetos en Python - parte 2

class Persona:
    def __init__(self):
        self.nombre = 'Elian'
        self.apellido = 'Amado'
        self.edad = 20

persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


# 3. Creación de Objetos con Argumentos

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Elian', 'Amado', 20)
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Julieta', 'Espinel', 15)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


# 4. Modificar Atributos de un Objeto

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Elian', 'Amado', 20)
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1.nombre = 'Alex'
persona1.apellido = 'Rivera'
persona1.edad = '25'

print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Julieta', 'Espinel', 15)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')


# 5. Métodos de Instancia en Python

class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Elian', 'Amado', 20, 'Hola', 20, 31, False, m = 'manzana', p = 'pera')
persona1.mostrar_detalle()

persona2 = Persona('Julieta', 'Espinel', 15)
persona2.mostrar_detalle()


# 6. Más de Self y Atributos de Instancia en Python

class Persona:
    def __init__(this, nombre, apellido, edad):
        this.nombre = nombre
        this.apellido = apellido
        this.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Elian', 'Amado', 20)
persona1.mostrar_detalle()
persona1.telefono = '3023749114'
print(persona1.telefono)
# Persona.mostrar_detalle(persona1)

persona2 = Persona('Julieta', 'Espinel', 15)
persona2.mostrar_detalle()
print(persona2.telefono)

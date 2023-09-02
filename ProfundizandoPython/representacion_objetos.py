# Representacion de objetos (str, repr, format)
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

    # repr, más enfocado a los programadores
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'

    # str es más para el usuario final u otros sistemas
    # la implementación por default llama al método repr
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # format su implementación por default es str
    # se manda a llamar al usar f-string
    def __format__(self, __format_spec: str) -> str:
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juan', 'Perez')
# repr (!r)
print(f'Mi objeto persona1: {persona1!r}')
# str (de manera automática el método print llama al método str)
print(persona1)
# format
print(f'{persona1}')


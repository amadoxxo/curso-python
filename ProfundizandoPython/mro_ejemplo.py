class Clase1:
    def __init__(self) -> None:
        print('Clase1.__init__')

    def metodo(self):
        print('Método de clase1')

class Clase2(Clase1):
    def __init__(self) -> None:
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Método de clase2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self) -> None:
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Método de clase3')
        super().metodo()

class Clase4(Clase3, Clase2):
    def metodo(self):
        print('Método de clase4')
        super().metodo()

# Creamos objeto de clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# mro
print(Clase4.__mro__)
# cual método se ejecuta
clase4.metodo()
from Computadora import Computadora
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Orden:
    
    contador_ordenes:int = 0
    
    def __init__(self, computadoras:Computadora) -> None:
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = list(computadoras)
    
    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras
    
    def agregar_computadora(self, computadora:Computadora):
        self._computadoras.append(computadora)
    
    def __str__(self) -> str:
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'Orden: {self._id_orden}, computadoras: {computadoras_str}'



if __name__ == '__main__':
    monitor1 = Monitor('Hp', '15 pulgadas')
    teclado1 = Teclado('Hp', 'usb')
    raton1 = Raton('Hp', 'usb')

    monitor2 = Monitor('Acer', '27 pulgadas')
    teclado2 = Teclado('Acer', 'bluetooth')
    raton2 = Raton('Acer', 'bluetooth')

    monitor3 = Monitor('Gamer', '45 pulgadas')
    teclado3 = Teclado('Gamer', 'bluetooth')
    raton3 = Raton('Gamer', 'bluetooth')

    computadora1 = Computadora('Hp', monitor1, teclado1, raton1)
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

    orden1 = Orden([computadora1, computadora2])
    orden2 = Orden([computadora3, computadora1])
    orden1.agregar_computadora(computadora3)

    print(orden1) 
    print(orden2)
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Computadora: 
    
    contador_computadoras:int = 0
    
    def __init__(self, nombre:str, monitor:Monitor, teclado:Teclado, raton:Raton) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor
        
    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado
        
    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self, raton):
        self._raton = raton
        
    def __str__(self) -> str:
        return f"""
        {self._nombre}: {self._id_computadora}
            {self._monitor} 
            {self._teclado}
            {self._raton}
        """


if __name__ == '__main__':
    monitor1 = Monitor('Hp', '15 pulgadas')
    teclado1 = Teclado('Hp', 'usb')
    raton1 = Raton('Hp', 'usb')

    monitor2 = Monitor('Acer', '27 pulgadas')
    teclado2 = Teclado('Acer', 'bluetooth')
    raton2 = Raton('Acer', 'bluetooth')

    computadora1 = Computadora('Hp', monitor1, teclado1, raton1)
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    print(computadora1)
    print(computadora2)
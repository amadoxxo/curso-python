class Monitor:
    
    contador_monitores:int = 0
    
    def __init__(self, marca:str, tamano:str) -> None:
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamano
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def tamano(self):
        return self._tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano
    
    def __str__(self) -> str:
        return f'Monitor: Id: {self._id_monitor}, marca: {self._marca}, tamaño: {self._tamano}'


if __name__ == '__main__':
    monitor1 = Monitor('LG', '27 pulgadas')
    monitor1.marca = 'Samsumng'
    monitor1.tamano = '16 pulgadas'
    monitor2 = Monitor('ASUS', '18 pulgadas')
    print(monitor1)
    print(monitor2)
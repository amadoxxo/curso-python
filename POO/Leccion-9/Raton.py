from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contador_ratones:int = 0
    
    def __init__(self, marca:str, tipo_entrada:str) -> None:
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self._id_ratones = Raton.contador_ratones
    
    def __str__(self) -> str:
        return f'Ratón: Id: {self._id_ratones}, {super().__str__()}'
    
if __name__ == '__main__':
    raton1 = Raton('USB', 'ASUS')
    raton1.tipo_entrada = 'Bluetooth'
    raton1.marca = 'Lenovo'
    raton2 = Raton('USB', 'RAZER')
    print(raton1)
    print(raton2)

from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclados:int = 0
    
    def __init__(self, marca:str, tipo_entrada:str) -> None:
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        
    def __str__(self) -> str:
        return f'Teclado: Id: {self._id_teclado}, {super().__str__()}'

if __name__ == '__main__':
    teclado1 = Teclado('Cable', 'Logitech')
    teclado1.tipo_entrada = 'Bluetooth'
    teclado1.marca = 'RAZER'
    teclado2 = Teclado('Cable', 'Coursair')
    print(teclado1)
    print(teclado2)
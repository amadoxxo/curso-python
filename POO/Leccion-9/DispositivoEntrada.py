class DispositivoEntrada:
    def __init__(self, marca:str, tipo_entrada:str) -> None:
        self.__marca = marca
        self.__tipo_entrada = tipo_entrada
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def tipo_entrada(self):
        return self.__tipo_entrada
    
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self.__tipo_entrada = tipo_entrada
        
    def __str__(self) -> str:
        return f'marca: {self.__marca}, tipo_entrada: {self.__tipo_entrada}'
    
if __name__ == '__main__':    
    dispositivoEntrada1 = DispositivoEntrada('USB', 'HP')
    dispositivoEntrada1.tipo_entrada = 'Bluetooth'
    dispositivoEntrada1.marca = 'ASUS'
    print(dispositivoEntrada1)

        
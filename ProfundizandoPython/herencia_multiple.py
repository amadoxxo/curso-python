# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos) -> None:
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]) -> None:
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]) -> None:
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validado los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un número entero: {elemento}')

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self ,elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)

# Lista de Enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

# Lista simple
lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
# Lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
# Lista enteros ordenada
lista_entero = ListaEnteros([1, 3, 4, -15])
print(lista_entero)
# Lista de enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5,-1, 10, 14, -4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
# MRO (Method Resolution Orden)
print(ListaEnterosOrdenada.__mro__)
# isinstance
print('Es entero?', isinstance(10, int))
print('Es cadena?', isinstance('hola', str))
print('Es lista ent ord?', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista ent?', isinstance(lista_enteros_ordenada, ListaEnteros))
print('Es lista ord?', isinstance(lista_enteros_ordenada, ListaOrdenada))
print('Es lista simple?', isinstance(lista_enteros_ordenada, ListaSimple))
print('Es object?', isinstance(lista_ordenada, object))
print('Es de varios tipos?', isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple)))
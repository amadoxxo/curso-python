class Producto:
    contador_productos = 0
    
    def __init__(self, nombre, precio) -> None:
        Producto.contador_productos += 1
        self._id_productos = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio
    
    def __str__(self) -> str:
        return f'ID: {self._id_productos}, Nombre: {self._nombre}, Precio: {self._precio}'
    
if __name__ == '__main__':
    producto1 = Producto('camisa', 15000)
    producto2 = Producto('zapatillas', 50000)
    print(producto1)
    print(producto2)
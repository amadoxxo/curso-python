from Producto import Producto

class Orden:
    contador_orden = 0
    
    def __init__(self, productos) -> None:
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)
    
    def agregar_productos(self, producto):
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self) -> str:
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__()+' | '
        return f'Orden: {self._id_orden}\nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Pantalon', 25000)
    producto2 = Producto('Mouse', 120000)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    orden2 = Orden(productos1)
    print(orden1)
    print(orden2)
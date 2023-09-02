from Producto import Producto
from Orden import Orden


producto1 = Producto('Pantalon', 25000)
producto2 = Producto('Mouse', 120000)
producto3 = Producto('Blusa', 50000)
producto4 = Producto('Medias', 12000)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_productos(producto3)
orden1.agregar_productos(producto4)
orden2 = Orden(productos2)
print(orden1)
print(orden1.calcular_total())
print(orden2)
print(orden2.calcular_total())
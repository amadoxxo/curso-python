from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creación del objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='Amarillo')
cuadrado1.ancho = 2
cuadrado1.alto = 2
print(f'El area del cuadrado es de: {cuadrado1.calcular_area()}')
print(cuadrado1)


print('Creación del objeto rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=8, alto=2, color='Rojo')
rectangulo1.ancho = 5
rectangulo1.alto = 25
print(f'El area del rectangulo es de: {rectangulo1.calcular_area()}')
print(rectangulo1)

# 2. Metodo MRO - Method Resolution Order en Python
# print(Cuadrado.mro())
# print(Rectangulo.mro())



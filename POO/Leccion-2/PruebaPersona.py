# 3. Uso de Módulos y Clases en Python

from Persona import Persona

print('Creación del objeto'.center(50, '-'))
persona1 = Persona('Stefanny', 'Casas', 20)
persona1.mostrar_detalle()
# print(__name__)
del persona1
print('Eliminación del objeto'.center(50, '-'))
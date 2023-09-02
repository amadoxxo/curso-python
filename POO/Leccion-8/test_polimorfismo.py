from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Elian', 1200000)
imprimir_detalles(empleado)

gerente = Gerente('Juan', 10000000, 'Arquitecto')
imprimir_detalles(gerente)

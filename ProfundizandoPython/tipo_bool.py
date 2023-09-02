# bool contiene los valores de True y False

# Tipos numericos, False para 0, True demás valores
valor = 0
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')
valor = 15
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Tipo str, False '', True demás valores
valor = ''
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Tipos colecciones, False para colecciones vacias, True para todas las demás colecciones
# Lista
valor = []
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')
valor = [2,3,4]
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')
valor = (2,3,4)
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')
valor = {'Nombre':'Juan', 'Apellido':'Perez'}
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

variable = 10
if bool(variable):
    print('Regreso verdadero')
else:
    print('Regreso falso')

if variable:
    print('Regreso verdadero')
else:
    print('Regreso falso')

while variable:
    print('ejecución ciclo while')
    break
else:
    print('fin ciclo while')
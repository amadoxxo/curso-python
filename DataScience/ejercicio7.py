# Ejercicio 7
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Lina Paola Barrera
# Elian Amado Ramirez

numeros_loteria = []

while len(numeros_loteria) <= 5:
    numeros_ganadores = int(input('Número ganadores de la lotería: '))
    numeros_loteria.append(numeros_ganadores)

numeros_loteria.sort()
print(f'Los números ganadores ordenados de menor a mayor son: {numeros_loteria}')
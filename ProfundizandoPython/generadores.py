# Generadores
# Es una función especial, retorna una secuencia de valores
# suspende la ejecucion de la función yield (producir) (no se usa return)

def generador():
    yield 1
    print(f'Se reanuda la ejecución')
    yield 2
    print(f'Se reanuda la ejecución')
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
# Si tratamos de consumir más valores de los que produce el generador
# lanza un error de StopIteration
# print(next(gen))


# Consumiendo los valores del generador con un ciclo for
for valor in generador():
    print(f'Número de generador: {valor}')
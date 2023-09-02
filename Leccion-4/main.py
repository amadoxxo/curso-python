# 1. Ciclo While en Python

# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')

contador = 0
while contador < 3:
    print(contador)
    contador += 1 #contador = contador + 1
else:
    print('Fin ciclo while')


# 2. Ciclo for en Python

cadena = 'Hola'

for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')


# 3. Palabra break en Python

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')


# 4. Palabra continue en Python

# for i in range(6):
#     if i % 2 == 0:
#         print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
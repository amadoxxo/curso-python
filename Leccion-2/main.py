# 1. Operadores Aritméticos en Python

operandoA = 3
operandoB = 2
suma = operandoA + operandoB
#print('Resultado suma:', suma)
print(f'Resultado suma: {suma} ')


# 2. Operadores Aritméticos en Python - parte 2

operandoA = 3
operandoB = 2
suma = operandoA + operandoB
#print('Resultado suma:', suma)
print(f'Resultado suma: {suma} ')
resta = operandoA - operandoB
print(f'Resultado resta: {resta} ')
multiplicacion = operandoA * operandoB
print(f'Resultado multiplicación: {multiplicacion}')
division = operandoA / operandoB
print(f'Resultado división: {division}')
division = operandoA // operandoB
print(f'Resultado división (int): {division}')
modulo = operandoA % operandoB
print(f'Resultado residuo división (módulo): {modulo}')
exponente = operandoA ** operandoB
print(f'Resultado exponente: {exponente}')


# 3. Operadores de Asignación en Python

miVariable = 10
print(miVariable)

miVariable = miVariable + 1
print(miVariable)
# incremento con reasignación
miVariable += 1
print(miVariable)
# miVariable = miVariable - 2
miVariable -= 2
print(miVariable)
# miVariable = miVariable * 3
miVariable *= 3
print(miVariable)

miVariable /= 2
print(miVariable)


# 4. Operadores de Comparación en Python

a = 4
b = 6

resultado = a == b
print(f'Resultado == : {resultado}')

resultado = a != b
print(f'Resultado != : {resultado}')

resultado = a > b
print(f'Resultado > : {resultado}')

resultado = a >= b
print(f'Resultado >= : {resultado}')

resultado = a < b
print(f'Resultado < : {resultado}')

resultado = a <= b
print(f'Resultado: <= {resultado}')


# 5. Ejercicio Número Par o Impar en Python

a = int(input('Escribe un valor numérico: '))

#print(a % 2)
if a % 2 == 0:
    print(f'El valor de a {a} es número par')
else:
    print(f'El valor de a {a} es número impar')


# 6. Ejercicio Determina si es Mayor de Edad 

edadAdulto = 18
edadPersona = int(input("Proporciona tu edad: "))

if edadPersona >= edadAdulto:
    print(f'La persona con edad {edadPersona} es un adulto')
else:
    print(f'La persona con edad {edadPersona} es menor de edad')


# 7. Operadores Lógicos en Python

a = True
b = False
resultado = a and b
# print(resultado)

resultado = a or b
# print(resultado)

resultado = not a
print(resultado)


# 8. Ejercicio - Valor dentro de Rango

valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

#dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
dentroRango = valor >= valorMinimo and valor <= valorMaximo

if dentroRango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')


# 9. Ejercicio - Operador or 

vacaciones = False
diaDescanso = True

if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')


# 10. Ejercicio - Operador not

vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')


# 11. Ejercicio - Rango entre 20's y 30's

edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad <40
#print(treintas)

if (edad >= 20 and edad < 30) or (edad >= 30 and edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
#    if veintes:
#        print('Dentro de los 20\'s')
#    elif treintas:
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de rango')
else:
    print("No está dentro de los 20's ni 30's")


# 12. Solución - Ejercicio Tienda de Libros

print('Proporcione los siguientes datos del libro: ')
nombre = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el ID del libro: '))
precio = float(input('Proporciona el valor de libro: '))
envioGratuito = input('Indica si es envío gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True/False'

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envío Gratuito?: {envioGratuito}
''')
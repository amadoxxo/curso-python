# 1. Funciones en Python

def mi_funcion():
     print('saludos desde mi función')

mi_funcion()


# 2. Paso de argumentos en Python

def mi_funcion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion('Juan', 'Perez')
mi_funcion('Karla','Lara')


# 3. Palabra Return en Funciones con Python

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f'Resultado sumar: {resultado}')
print(f'Resultado sumar: {sumar(5,3)}')


# 4. Valores por Default en los Parámetros de una Función

def sumar(a = 0, b = 0):
    return a + b

resultado = sumar()
print(f'Resultado sumar: {resultado}')

print(f'Resultado sumar: {sumar(2,8)}')


# 5. Argumentos Variables en Funciones con Python

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'María', 'Ernesto')
listarNombres('Laura', 'Carlos')


# 6. Argumentos Variables llave-valor en Python

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')


# 7. Distintos tipos de datos como argumentos en Python

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8, 9))
desplegarNombres([10, 11])


# 8. Funciones Recursivas en Python

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')
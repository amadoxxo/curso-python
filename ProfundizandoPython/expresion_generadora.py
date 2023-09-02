# Expresión generadora (es un generador anónimo)
multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# También se puede pasar una expresión generadora a una función (sin paréntesis) 
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

# También podemos usar una lista a cualquier otro iterador
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a partir de un generador creado a partir de una lista
nombres = ['Laura', 'Camila', 22]
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

generador = (f'{incrementar()}. {nombre}' for nombre in nombres)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')
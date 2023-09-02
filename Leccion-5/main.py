# 1. Listas en Python

# Definir una lista de tipo str
nombres = ['Juan','Karla','Ricardo', 'María']
# imprimir la lista nombres
print(nombres)
# acceder a los elementos de un a lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])


# 2. Listas en Python - parte 2

#Imprimir un rago
print(nombres[0:2]) # sin incluir el índice 2
#Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
#Desde el índice indicado hasta el final
print(nombres[1:])
#Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen más nombres en la lista')


# 3. Listas en Python - parte 3

# preguntar el largo de una lista
print(len(nombres))
# agregar un elemento
nombres.append('Lorenzo')
print(nombres)
# insertar un elemento en un índice en específico
nombres.insert(1, 'Octavio')
print(nombres)
# remover un elemento
nombres.remove('Octavio')
print(nombres)
# remover el último valor agregado
nombres.pop()
print(nombres)
# eliminar un indice
del nombres[0]
print(nombres)
# limpiar la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)


# 4. Tuplas en Python

#Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
# navegación inversa
print(frutas[-1])
# acceder a un rango
print(frutas[0:1])# sin incluir el último índice


# 5. Tuplas en Python - parte 2

#recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor tupla
# frutas[0] = 'Pera'
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
#eliminar la tupla
del frutas
print(frutas)


# 6. Set en Python

# set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
# revisar si un elemento está presente
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print( planetas)
#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
# eliminar elemento sin arrojar error
planetas.discard('Júpiters')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar el set
del planetas
print(planetas)


# 7. Diccionarios en Python

# dict (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
# acceder a un elemento (key)
print( diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
# modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)


# 8. Diccionarios en Python - parte 2

# recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algún elemento
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# limpiar
diccionario.clear()
print(diccionario)

# eliminar el diccionario
del diccionario
print(diccionario)

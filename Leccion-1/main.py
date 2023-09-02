# 1. Hola mundo con Python

print("Hola Mundo con Python")


# 2. Variables en Python

miVariable = 2
print( miVariable )
print( miVariable )
print( miVariable )

miVariable = 10
print( miVariable )


# 3. Variables en Python - parte 2

x = 10
y = 2
z = x + y
print(x)
print(y)
print(z)

 
# 4. Dirección de Memoria y Variables en Python

x = 10
y = 2
z = x + y
print(x)
print(y)
print(z)
print(id(x))
print(id(y))
print(id(z))


# 5. Tipos de Datos en Python

x = False
print(x)
print(type(x))
 
# 6. Resumen Tipos de Datos en Python

#Tipo int
x = 10
print(x)
print(type(x))
#Tipo float
x = 14.5
print(type(x))
#Tipo String
x = 'Hola Mundo'
print(type(x))
#Tipo bool 
x = True
print(type(x))
x = False
print(type(x))


# 7. Manejo de Cadenas en Python

#Cadena (String)
miGrupoFavorito = "Metallica"
comentario = "The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)


# 8. Más Temas de Manejo de Cadenas 

# Cadena (String)
miGrupoFavorito = "Metallica"
comentario = "The Best Rock Band"
# print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)
print("Mi grupo favorito es:", miGrupoFavorito, comentario)

numero1 = "1"
numero2 = "2"
print("Concatenación:", numero1 + numero2)
print("Suma:", int(numero1) + int(numero2))

# numero1 = 1
# numero2 = 2
# print(numero1 + numero2)


# 9. Tipos de Boleanos (bool) en Python

# Tipos bool (boolean)
miVariable = False
print(miVariable)

miVariable = 3 > 2
print(miVariable)

if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")


# 10. Procesar Entrada del Usuario (Función input)

# Función input para procesar la entrada del usuario
resultado = input("Escribe un mensaje: ")
print("Valor proporcionado:",resultado)
print("Fin del programa")


# 11. Conversión de la Entrada de Datos en Python

# Función input para procesar la entrada del usuario
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es:", resultado)


# 12. Solución Ejercicio Califica tu Día

# Califica tu dia del 1 al 10
resultado = int(input('Cómo estuvo tu día (1 al 10)?: '))
print('Mi día estuvo de:', resultado)

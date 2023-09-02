# Ejercicio 4
# Escribir un programa que pregunte el nombre del usuario en la consola y
# después de que el usuario lo introduzca muestre por pantalla<NOMBRE> tiene <n> letras,
# donde<NOMBRE>es el nombre de usuario en mayúsculas y<n>es el número de letras que tienen el nombre.

# Lina Paola Barrera
# Elian Amado Ramirez

nombre = input(str('Nombre: '))
numero_letras = len(nombre)
nombre_mayusculas = nombre.upper()

print(f'{nombre_mayusculas} tiene el número de letras: {numero_letras}')
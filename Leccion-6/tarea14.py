# Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos
# variables *args como parámetro de la función y regresar como resultado la multiplicación de todos
# los valores pasados como argumentos.

# Definición de la función para multiplicar valores
def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

# Llamada de la función
print(multiplicar_valores(5,6,3))
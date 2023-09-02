# Crear una función para sumar los valores recibidos de tipo numérico, utilizando
# argumentos variables *args como parámetro de la función y regresar como resultado
# la suma de todos los valores pasados como argumentos.

#Definición de la función para sumar valores
def sumar_valores(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

#LLamada de la función
print(sumar_valores(3,5,9))
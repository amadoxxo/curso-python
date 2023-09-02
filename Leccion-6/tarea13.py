# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

# Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a 
# fahrenheit

#     La función se llama: celsius_fahrenheit(celsius) 

#     La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32  

# Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a 
# celsius:

#     fahrenheit_celsius(fahrenheit)         

#     La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9

# Los valores los debe proporcionar el usuario, utilizando la función input y
# convirtiendolo a tipo float.

# Deben hacer al menos dos pruebas, una donde conviertan de grados celcius a
# grados fahrenheit, y otra donde conviertan de grados fahrenheit a grados celsius y
# mandar a imprimir los resultados.

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
        return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
        return (fahrenheit-32) * 5/9

# Realizamos algunas pruebas de conversión
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Los dos puntos después de la variable de resultado dan un formato de 2 digitos flotantes
print(f'{celsius} C a F: {resultado:.2f}')
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C: {resultado:.2f}')
# 1. Sentencia If/Else en Python

condicion = False

if condicion == True:
    print('Condición verdadera')
elif condicion == False:
    print('Condición falsa')
else:
    print('Condición no reconocida')


# 2. Ejercicio - Conversión de Número a Texto en Python

numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto = ''
if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'
print(f'Número proporcionado: {numero} - {numeroTexto}')


# 3. Sintáxis if else simplificada (Operador Ternario)

condicion = False

# if condicion:
#     print('Condición verdadera')
# else:
#     print('Condición falsa')

print('Condición verdadera') if condicion else print('Condición falsa') 


# 4. Ejercicio - Calcular la Estación según el Mes Proporcionado

mes = int(input('Proporciona mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estación es: {estacion}')


# 5. Solución Ejercicio Etapas de Vida según Edad

edad = int(input('Proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increíble...'
elif  10 <= edad < 20:
    mensaje = 'Muchos cambios, mucho estudio...'
elif  20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida NO reconocida'
print(f'Tu edad es: {edad}, {mensaje}')
# Ejercicio 2
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice  de  masa  corporal  y  lo  almacene  en  una  variable,
# y  muestre  por  pantalla  la  frase Tu índice  de  masa  corporal  es  <imc>donde<imc>es  el  índice
# de  masa  corporal  calculado redondeado con dos decimales.

# Lina Paola Barrera
# Elian Amado Ramirez

peso = float(input('Peso(kg): '))
altura = float(input('Estatura(metros): '))

res = peso / altura**2

print(f'Tu índice  de  masa  corporal: {res:.2f}')
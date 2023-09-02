# Ejercicio 1 
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

# Lina Paola Barrera
# Elian Amado Ramirez

numero_trabajo = float(input('Número des horas trabajadas?: '))
coste_hora = float(input('Coste por hora: '))

res = numero_trabajo * coste_hora

print(f'La paga correspondiente es de: {res}')
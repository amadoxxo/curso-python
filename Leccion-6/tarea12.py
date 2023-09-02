# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.

# La función se llama calcular_total()

# La función recibe dos parámetros:

# 1. pago_sin_impuesto

# 2. impuesto (Ej. Valor de 10, significa 10% de impuesto, Valor de 16 significa el 16% de impuesto)

# La función debe regresar el total del pago incluyendo el porcentaje de impuesto
# proporcionado.

# Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0

# Los valores los debe proporcionar el usuario y se procesados con la función input,
# convirtiendolos a tipo float.

# Función que calcula el impuesto de un pago
def calcular_total(pago_sin_impuesto, impuesto):
    return pago_sin_impuesto + pago_sin_impuesto*(impuesto/100)

# Ejecutamos la función
pago_sin_impuesto = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_total(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')
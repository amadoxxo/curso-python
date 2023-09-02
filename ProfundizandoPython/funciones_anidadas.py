# Calculadora
def calculadora(a,b, operacion='sumar'):
    # 1. Definir Función anidada
    def sumar(a,b):
        return a + b

    def restar(a,b):
        return a - b

    # 2. Llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado suma: {sumar(a,b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a,b)}')

calculadora(5,6, operacion='restar')
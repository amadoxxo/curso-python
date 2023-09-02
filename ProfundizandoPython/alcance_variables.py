# variables globales
var_global = 'Variable global'

def imprimir():
    # Acceder a una variable global
    global var_global
    print(f'Variable global desde función: {var_global}')
    # Defenición de variable local
    var_local = 'Variable local'
    print(f'Variable local desde función: {var_local}')
    var_global = 'Nuevo valor'

    def funcion_anidada():
        print(f'Variable local dentro de función anidada: {var_local}')

    funcion_anidada()


imprimir()
print(f'Var global fuera función: {var_global}')
datos_usuario = dict()

def diccionario(llave, valor):
    datos_usuario[llave] = valor
    print(datos_usuario)

# nombre
nombre = str(input('Ingrese un nombre: '))
diccionario('nombre', nombre)
# edad
edad = int(input('Ingrese una edad: '))
diccionario('edad', edad)
# sexo
sexo = str(input('Ingrese un sexo: '))
diccionario('sexo', sexo)
# telefono
telefono = str(input('Ingrese un número telefonico: '))
diccionario('telefono', telefono)
# email
email = str(input('Ingrese un email: '))
diccionario('email', email)
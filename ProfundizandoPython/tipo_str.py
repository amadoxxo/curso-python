# Profundizando en el tipo str

# Concatenación automática en python
variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
mensaje += 'Universidad' 'Python'
# print(mensaje)

import math
from mi_clase import MiClase

# help(math.isnan)
# help(str.capitalize)

# help(MiClase)
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))

mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
# print(f'Mensaje1: {mensaje1}, id{hex(id(mensaje1))}')
# print(f'Mensaje2: {mensaje2}, id{hex(id(mensaje2))}')
mensaje1 += 'adios'
# print(f'Mensaje1: {mensaje1}, id{hex(id(mensaje1))}')

# help(str.join)

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
# print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
# print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
# print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
# print(f'llaves: {llaves} type: {type(llaves)}')
# print(f'valores: {valores} type: {type(valores)}')

# help(str.split)

cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
# print(f'lista cursos: {lista_cursos}')
# print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
# print(f'lista cursos: {lista_cursos}')
# print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(', ', 3)
# print(f'lista cursos: {lista_cursos}')
# print(len(lista_cursos))

nombre = 'Juan'
edad = 28

mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)
# print(mensaje_con_formato)

persona = ('Karla', 'Gomez', 5000.00)
# mensaje_con_formato = 'Mi nombre es %s %s y tengo %.2f años'%persona
# print(mensaje_con_formato)
mensaje_con_formato = 'Mi nombre es %s %s y tengo %.2f años'
# print(mensaje_con_formato%persona)

nombre = 'Juan'
edad = 28
sueldo = 3000

mensaje = 'Nombre {} Edad {} sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'Nombre {0} Edad {1} sueldo {2:.2f}'.format(nombre, edad, sueldo)
# print(mensaje)

mensaje = 'sueldo {2:.2f} Nombre {0} Edad {1}'.format(nombre, edad, sueldo)

# print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s}'.format(n=nombre, e=edad, s=sueldo)

# print(mensaje)

diccionario = {'nombre': 'Juan', 'edad': 35, 'sueldo': 3000}

mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)

# print(mensaje)

mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'

# print(mensaje)

# Metodo print
# print(nombre, edad, sueldo, sep=', ')

# multiplación str
resultado = 5*'hola'
# print(f'Resultado: {resultado}')

# multiplicación tuplas
resultado = 5*('Hola', 10)
# print(f'Resultado: {resultado}')

# multiplicación de listas
resultado = 10*[0]
# print(f'Resultado: {resultado}, largo: {len(resultado)}')

# caracteres de escape
resultado = 'Hola\' mundo'
# print(f'Resultado: {resultado}')

resultado = 'Se va eliminar el punto.\b\b\b'
# print(f'Resultado: {resultado}')

# caracter con \
resultado = 'c:\\nuevo\\juan'
# print(f'Resultado: {resultado}')

# raw string
resultado = r'Cadena con \n salto de linea'
# print(f'Resultado: {resultado}')

resultado = R'c:\nuevo\juan'
# print(f'Resultado: {resultado}')

# caracteres unicode
# print('Hola\u0020Mundo')
# print('Notación simple:', '\u0041')
# print('Notación extendida:', '\U00000041')
# print('Notación hexadecimal:', '\x41')
# print('Corazón:', '\u2665')
# print('Cara sonriendo:', '\U0001f600')
# print('Serpiente', '\U0001F40D')

# Caracteres ascii
caracter = chr(65)
# print('A mayúscula:',caracter)
caracter = chr(64)
# print('Simbolo @:',caracter)
caracter = chr(97)
# print('a minuscula:',caracter)

# caracteres bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_de_caracteres = mensaje.split()
print(lista_de_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado:',bytes)
# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:',string2)
print(string == string2)
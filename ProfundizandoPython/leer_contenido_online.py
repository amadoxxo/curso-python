# Leer contenido online
import urllib.request
from urllib.request import urlopen

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

req = urllib.request.Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt', headers = headers)

with urlopen(req) as mensaje:
    # contenido = mensaje.read()
    contenido = mensaje.read().decode('utf-8')
    # print(contenido)
    # palabras = []
    # for linea in mensaje:
        # palabras_por_linea = linea.decode('utf-8').split()
        # for palabra in palabras_por_linea:
            # palabras.append(palabra)

# print(palabras)

# with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
    # archivo.write(contenido)

# Contar ocurrencias de una cadena
print('No. veces Universidad:',contenido.count('Universidad'))

# uppper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# lower convierte a minúsculas un str
print(contenido.lower())

# buscamos la cadena python en el contenido
print('Existe python?:', 'python'.lower() in contenido.lower())
print('Existe python?:', 'python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con: ', contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con:', contenido.lower().endswith('globalmentoring.com.mx'.lower()))

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

# center - Centrar un str
titulo = 'Sitio web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(50, '*'))
print(titulo.center(len(titulo)+10,'-'))

# ljust - alinea a la izquierda
# print(titulo.ljust(50, '*'))
print(titulo.ljust(len(titulo)+10, '-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+10, '-'))

# Reemplazar contenido en str
print(contenido.replace(' ', '-'))

# Eliminar caracteres al inicio y final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original:',titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada',titulo, len(titulo))
titulo = '*** GlobalMentoring.com.mx ***'.strip('')
print('Cadena modificada', titulo)
titulo = '***GlobalMentoring***'.lstrip('*')
print('Cadena modificada', titulo)
titulo = '***GlobalMentoring***'.rstrip('*')
print('Cadena modificada', titulo)

titulo = ' *** GlobalMentoring *** '.strip().strip('*').strip()
print('Cadena modificada', titulo)



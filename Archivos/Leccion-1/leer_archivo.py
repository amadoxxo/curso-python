# archivo = open('C:\\Users\\elian\\OneDrive\\Escritorio\\python\\prueba.txt', 'r', encoding='utf8')
archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

# leer algunos carecteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#     print(linea)
    
# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
# print(archivo.readlines()[1])

# abrimos un nuevo archivo
# a - anexar información
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close() 
archivo2.close() 
print('Se ha terminado el proceso de leer y copiar archivos')

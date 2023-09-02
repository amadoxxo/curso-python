diccionario = {}
frase = input('Introduce la lista de palabras y traducciones en formato <palabra:traducción> separadas por comas(, ): \n')

for i in frase.split(', '):
    esp, eng = i.split(':')
    diccionario[esp] = eng

comprobacion = [input('Introduce una frase en español: ')]

for i in comprobacion:
    if i in diccionario:
        print(diccionario[i])
    else:
        print(i)
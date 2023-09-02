# Nombramos nuestro archivo .txt donde queremos almacenar el poema
poem = 'poem.txt'

# Utilizamos la función open para escribir el poema que queremos
poem_write = open(poem, 'w', encoding='utf8')
# Se escribe el poema
poem_write.write('Once there was an elephant,\n'
    'Who tried to use the telephant—\n'
    'No! No! I mean an elephone\n'
    'Who tried to use the telephone—\n'
    '(Dear me! I am not certain quite\n'
    'That even now I’ve got it right.)\n'
    'Howe’er it was, he got his trunk\n'
    'Entangled in the telephunk;\n'
    'The more he tried to get it free,\n'
    'The louder buzzed the telephee—\n'
    '(I fear I’d better drop the song\n'
    'Of elephop and telephong!)')

# Cerramos la función write para no sobreescribir el archivo
poem_write.close()

# Llamamos de nuevo la función open pero esta vez para que lea el archivo poem.txt
with open(poem, 'r', encoding='utf8') as archivo:

    # Con esta función regramos un str donde devuelve las lineas del poema que el usuario pida
    def count_lines( index ):
        return '\n'.join(archivo.readlines()[ :index ])
    
    # Se creo esta función para volver a llamar la función open ya que se utilizara de nuevo para imprimir
    # las lineas del poema
    def open_read(index):
        archivo2 = open(poem, 'r', encoding='utf8')
        return '\n'.join(archivo2.readlines()[ :index ])
    
    # Listas creadas para obtener o remover vocales, conosonantes y caracteres especiales
    vowels = ['a', 'e', 'i', 'o', 'u']
    characters = [' ', '!', ',', '\n', '—', '(', ')', '’', '.', ';']
    # Listas creadas para almacenar las vocales y consonantes
    vowels2 = []
    consonants = []

    lines = int(input('How many lines will you here? '))

    def num_of(lines):
        # Se obtiene cada letra del poema en minuscula para obtener tambien las letras que se encuetren
        # en mayuscula
        for i in count_lines(lines).lower():

            # Se itera la lista de vocales
            for j in vowels:
                # Se pregunta si por cada letra del poema se encuetra una vocal para luego agregarla a una
                # nueva lista
                if i is j:
                    vowels2.append(i)
            
            # Se pregunta si por cada letra del poema no se encuentra ninguna letra que no sea vocal
            # para agregarlo a la lista de consonantes
            if i not in vowels:
                consonants.append(i)

            # Se pregunta si por cada letra del poema se encuentra una letra que sea caracter
            # especial para removerlo de la lista de consonantes
            if i in characters:
                consonants.remove(i)

    num_of(lines)
    result = open_read(lines)
    print(result)
    print('Number of vowels: ', len(vowels2))
    print('Number of consonants: ', len(consonants))

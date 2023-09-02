# Leer archivo JSON
# JSON = JavaScript Object None
import json
from urllib.request import Request, urlopen


URL = Request('http://globalmentoring.com.mx/api/personas.json')
URL.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')

respuesta = urlopen(URL)
print(respuesta)
cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)
# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)
# Imprimir sólo los nombres de las personas
# JSON se convierte a listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona {persona["nombre"]} {persona["edad"]}')
# Accedemos a las variables independientes
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Total de personas: {json_respuesta["mensaje"]}')
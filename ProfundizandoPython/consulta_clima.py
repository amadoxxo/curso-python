import json
from urllib.request import Request, urlopen

URL = Request('http://globalmentoring.com.mx/api/clima.json')
URL.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')

respuesta = urlopen(URL)
# print(respuesta)
cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
# print(json_respuesta)
# Ejercicio 1. Acceder a la descripción del clima
# descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripcion clima: {descripcion_clima}')
# Ejercicio 2. Mostrar la temperatura mínima y máxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura mínima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura máxima: {temp_max}')
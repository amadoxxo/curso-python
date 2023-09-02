import os
from dominio.Pelicula import Pelicula

class CatalogoPeliculas:
    
    ruta_archivo:str = 'pelicula.txt'
    
    @classmethod
    def agregar_pelicula(cls, pelicula:Pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')
    
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catálogo de Películas'.center(50, '-'))
            print(archivo.read())
    
    @classmethod
    def eliminar_archivo(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
from dominio.Pelicula import Pelicula

opcion = None

while opcion != 4:
    try:
        print('1. Agregar Película')
        print('2. Listar Películas')
        print('3. Eliminar catálogo Películas')
        print('4. Salir')
        opcion = int(input('Escribe tu opción (1-4): '))

        if opcion == 1:
            nombre_pelicula = str(input('Proporciona la película: '))
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_archivo()
    
    except Exception as e:
        print(f'Ha ocurrido un error {e}')
else:
    print('Has salido del programa...')
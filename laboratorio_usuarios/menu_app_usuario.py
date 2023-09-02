from Usuario import Usuario
from logger_base import log
from UsuarioDAO import UsuarioDAO

opciones = None

while opciones != 5:
    print('Opciones:')
    print('1. Listar usuarios:')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opciones = int(input('Escribe tu opción (1-5): '))

    if opciones == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opciones == 2:
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(username=username, password=password)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')

    elif opciones == 3:
        id_usuario = input('Escribe el id_usuario a modificar: ')
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        usuario = Usuario(id_usuario, username, password)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios insertados: {usuarios_actualizados}')

    elif opciones == 4:
        id_usuario = input('Escribe el id_usuario a eliminar: ')
        usuario = Usuario(id_usuario)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
else:
    log.info('Salimos de la aplicación...')


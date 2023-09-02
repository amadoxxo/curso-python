from cursor_del_pool import CursorDelPool
from Usuario import Usuario
from logger_base import log

class UsuarioDAO:
    _SELECIONAR:str = 'SELECT * FROM usuario'
    _INSERTAR:str = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR:str = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR:str = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario:Usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario:Usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario:Usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':

    # Insertar Usuario
    # usuario1 = Usuario(username='ariveros', password='aleja123')
    # usuarios_insertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # Actualizar Usuario
    # usuario1 = Usuario(3, 'alejandra', 'holakases')
    # usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    # log.debug(f'Usuarios actualizados: {usuarios_actualizados}')

    # Eliminar Registro
    # usuario1 = Usuario(2)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Usuarios eliminados: {usuarios_eliminados}')


    # Seleccionar Objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
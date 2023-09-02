from Conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self) -> None:
        self._conn:str = None
        self._cursor:str = None

    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug(f'Se ejecuta metodo __exit__ with')
        if valor_excepcion:
            self._conn.rollback()
            log.error(f'Ocurrio una excepción {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conn.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conn)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())
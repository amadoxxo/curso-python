import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # conexion.autocommit = False
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Nicolas', 'Hernandez', 'nhernandez@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Ana', 'Vargas', 'avargas@mail.com', 11)
            cursor.execute(sentencia, valores)
            # conexion.commit()
except Exception as e:
    print(f'Ocurrió un error, se hizo rollback de la transacción: {e}')
finally:
    conexion.close()

print('Termina la transacción se hizo commit')
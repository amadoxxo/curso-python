# import psycopg2
import mysql.connector

conexion = mysql.connector.connect(
    # host='bi0qgprrgzixu2n7nmsi-mysql.services.clever-cloud.com',
    # user='uawwgqhehvnrv1k5',
    # password='Ue6msOYW2ztZoYHlZST8',
    # database='bi0qgprrgzixu2n7nmsi'
    host='betskrybq9ax2t60684q-mysql.services.clever-cloud.com',
    user='ubmvwdh7f9eulsy0',
    password='MeUAAx7euYfhV2CYYHdE',
    database='betskrybq9ax2t60684q'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # sentencia = 'SELECT * FROM docu_poli'
            sentencia = 'INSERT INTO peliculas_accion(nombre) VALUES(%s)'
            # sentencia = 'UPDATE docu_poli SET nombre=%s, director=%s WHERE id_docu'
            # sentencia = 'DELETE FROM docu_poli WHERE id_docu=%s'
            valores = ('PRUEBA.TXT',)
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_eliminado = cursor.rowcount
            print(f'Registros Actualizados: {registros_eliminado}')
            # registros = cursor.fetchall()
            # for registro in registros:
                # print(registro)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
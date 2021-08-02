import psycopg2 as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    """ UTILIZAR EL WITH ES UNA MEJOR PRACTICA"""

    #Con with ya aplica plica el concepto de transacciones 
    #Realiza el commit() y el rollback() automatico
    with conexion: 
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Alex', 'Rojas1235465132', 'arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez','jperez@mail.com', 1)
            cursor.execute(sentencia, valores)

            print('Termina la transacción, se hizo commit')
except Exception as e:
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()

    
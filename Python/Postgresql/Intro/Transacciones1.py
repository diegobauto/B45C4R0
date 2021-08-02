import psycopg2 as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    # conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)
    
    conexion.commit() #Guardar los registros
    print('Termina la transacción')

except Exception as e:
    conexion.rollback() #No guarda nada, ya que hubo un fallo
    print(f'Ocurrió un error, se hizo rollback: {e}')
finally:
    conexion.close()
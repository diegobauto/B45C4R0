import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM persona"
            cursor.execute(consulta)
            registros = cursor.fetchall() #Obtenemos todos los registros que retorna el cursor
            print(registros) #Mostramos los datos
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close() #Cerramos la conexion
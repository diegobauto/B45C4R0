import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM persona WHERE id_persona IN %s"
            valores = (tuple(["8","9"]),) #Debe ser una tupla de valores
            cursor.execute(consulta, valores) 
            registros_eliminados = cursor.rowcount #Saber el numero de registros eliminados
            print(f"Registros Eliminados: {registros_eliminados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
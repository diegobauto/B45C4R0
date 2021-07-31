import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM persona WHERE id_persona = %s"
            valores =  (2,) #Debe ser una tupla
            cursor.execute(consulta, valores)
            registro_eliminado = cursor.rowcount #Saber el numero de registros eliminados
            print(f"Registro Eliminado: {registro_eliminado}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
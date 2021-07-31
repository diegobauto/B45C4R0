import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "UPDATE persona SET nombre=%s, apellido=%s, emaiL=%s WHERE id_persona= %s"
            valores = ("Ana Maria", "Juarez", "nuevocorreo@email.com", 1) #Debe ser una tupla de valores
            cursor.execute(consulta, valores) 
            registro_actualizado = cursor.rowcount #Saber el numero de registros actualizados
            print(f"Registro Actualizado: {registro_actualizado}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM persona WHERE id_persona IN %s"
            entrada = input("Digite los id's (separado por comas): ")
            ids = (tuple(entrada.split(",")),)
            cursor.execute(consulta, ids)
            registros = cursor.fetchall() #Obtenemos todos los registros que retorna el cursor
            #Mostramos los datos
            for registro in registros:
               print(registro)
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close() #Cerramos la conexion
import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "SELECT nombre, apellido FROM persona WHERE id_persona = %s"
            idPersona = input("Digite el idPersona a consultar: ")
            cursor.execute(consulta, (idPersona,))
            registros = cursor.fetchone() #Obtenemos un registro que retorna el cursor
            print(registros) #Mostramos los datos
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close() #Cerramos la conexion
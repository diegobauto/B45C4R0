import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

#Creamos un cursor que nos permite ejecutae las consultas
cursor = conexion.cursor()

consulta = "SELECT * FROM persona"
cursor.execute(consulta)
registros = cursor.fetchall() #Obtenemos todos los registros que retorna el cursor

print(registros) #Mostramos los datos

cursor.close() #Cerramos el cursor
conexion.close() #Cerramos la conexion
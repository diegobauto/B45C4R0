import psycopg2 #Toca instalarlo

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            nombre = input("Digite el nombre: ")
            apellido = input("Digite el apellido: ")
            email = input("Digite el email: ")
            consulta = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = (nombre, apellido, email) #Debe ser una tupla de valores
            cursor.execute(consulta, valores)
            #conexion.commit() # Guarda los cambios en la base de datos, al usar with lo hace automatico
            registro_insertado = cursor.rowcount #Saber el numero de registros insertados
            print(f"Registro Instertado: {registro_insertado}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
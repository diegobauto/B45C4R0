import psycopg2

#Creamos la conexion a la base de datos
conexion = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = (
                ("Andres", "Boca", "abrebocas@email.com"), 
                ("Luisa", "Betancour", "lbcour@email.com")
            ) #Debe ser una tupla de valores
            cursor.executemany(consulta, valores) #Para ejecutar varias consultas (many)
            #conexion.commit() # Guarda los cambios en la base de datos, al usar with lo hace automatico
            registros_insertados = cursor.rowcount #Saber el numero de registros insertados
            print(f"Registros Instertados: {registros_insertados}")
except Exception as e:
    print(f"Ocurrio un error: {e}")
finally:
    conexion.close()
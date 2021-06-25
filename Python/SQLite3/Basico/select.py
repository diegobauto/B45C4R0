import sqlite3

#Nos conectamos a la base de datos, si no esta creada, crea una,
#y lo asignamos a cualquier variable
db = sqlite3.connect("Python\\SQLite3\\base.db")

#Necesitamos crear un cursor para realizar consultas
cursor = db.cursor()
cursor.execute("SELECT * FROM personas")

# fetchall() trae todos los registros
# fetchone() trae el primer registo como tupla
#fetchmany() trar el primer registro como lista
print(cursor.fetchall())

#Cerrar el cursos y liberar datos de la memoria
cursor.close()
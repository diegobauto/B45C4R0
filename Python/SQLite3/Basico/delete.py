import sqlite3

#Nos conectamos a la base de datos, si no esta creada, crea una,
#y lo asignamos a cualquier variable
db = sqlite3.connect("Python\\SQLite3\\base.db")

#Necesitamos crear un cursor para realizar consultas
cursor = db.cursor()

#Ejecuta la consulta
cursor.execute("DELETE FROM personas WHERE id=12")

#Cerrar el cursos y liberar datos de la memoria
cursor.close()

#Ejecuta los comandos que hay en los cursores
db.commit()
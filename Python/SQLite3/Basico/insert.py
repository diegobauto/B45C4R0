import sqlite3

#Nos conectamos a la base de datos, si no esta creada, crea una,
#y lo asignamos a cualquier variable
db = sqlite3.connect("Python\\SQLite3\\base.db")

#Necesitamos crear un cursor para realizar consultas
cursor = db.cursor()
cursor.execute("INSERT INTO personas(nombre, apellido, dni) VALUES ('Ana','Cayetana',33333333)")

""" SEGUNDA OPCION
registro = ('Carla', 'Bustamante', 55)
cursor.execute("INSERT INTO personas(nombre, apellido, dni) VALUES (?, ?, ?)", registro)
"""

""" PARA VARIOS REGISTROS
registros = [
    ('Juan', 'Perez', 1111),
    ('Lu', 'Gonzales', 2222),
    ('Laura', "Queedo", 3333),
    ('Leo', "Peralta", 4444)
]

cursor.executemany("INSERT INTO personas(nombre, apellido, dni) VALUES (?, ?, ?)", registro)
"""

#Ejecuta los comandos que hay en los cursores
db.commit()


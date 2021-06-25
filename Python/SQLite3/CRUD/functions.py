import sqlite3 

def connection():
    try:
        db = sqlite3.connect("Python\SQLite3\CRUD\data.db")
        return db, db.cursor()
    except:
        print("No se pudo realizar la conexion")


def create():
    #Obtengo la base de datos y obtengo el cursor para realizar las consultas
    db,cursor = connection()

    print("\n-- Crear Registo --")
    nombre = ""
    apellido = ""
    while nombre.isalpha()==False or 50<=len(nombre)<3 or 50<=len(apellido)<3 or apellido.isalpha()==False:
        nombre = input("Digite el nombre: ")
        apellido = input("Digite el apellido: ")
    cursor.execute("INSERT INTO Persona(nombre, apellido) VALUES (?,?)", (nombre, apellido))
    cursor.close()
    db.commit()
    print("**Añadido correctamente**")

    #Conexion finalizada
    db.close()


def read():
    #Obtengo la base de datos y obtengo el cursor para realizar las consultas
    db,cursor = connection()

    print("\n-- Ver Resgistro --")
    id = input("Digite el id: ")
    if id.isnumeric():
        #Realizamos la consulta con el id digitado
        cursor.execute(f"SELECT * FROM Persona WHERE id='{id}'")
        dato = cursor.fetchone()
        cursor.close()
        db.close()
        #Se 'comprueba' si el id existe en la base de datos, verificando si devuelve algo
        if dato != None:
            print(dato)
            return dato
        else:
            print("No existe registros con ese id en la base de datos")
    else:
        print("Digito un id invalido")


def readAll():
    #Obtengo la base de datos y obtengo el cursor para realizar las consultas
    db,cursor = connection()

    cursor.execute("SELECT * FROM Persona")
    # Traer los registros
    dato = cursor.fetchall()
    
    #Si hay datos, o registros dentro de la base de datos, los muestra, sino muestra un mensaje
    if dato:
        print("\n-- Ver Resgistros --")
        print(dato)
        cursor.close()
        db.close()
    else:
        print("No hay registros en la base de datos")


def update():
    #Obtengo la base de datos y obtengo el cursor para realizar las consultas
    db,cursor = connection()

    print("\n-- Actualizar Resgistro --")
    # Traer el dato que quiero buscar de la funcion read()
    dato = read()
    #Si hay dato, si contiene algun valor
    if dato:
        #Pedimos los datos
        nombre = input("Digite el nombre a cambiar: ")
        apellido = input("Digite el apellido a cambiar: ")
        #Realizamos la consulta para actualizar
        cursor.execute(f"UPDATE Persona SET nombre='{nombre}',apellido='{apellido}' WHERE id={dato[0]}")
        db.commit()
        print("**Actualizado correctamente**")
    cursor.close()
    db.close()


def delete():
    #Obtengo la base de datos y obtengo el cursor para realizar las consultas
    db,cursor = connection()

    print("\n-- Eliminar Resgistro --")
    # Traer el dato que quiero buscar de la funcion read()
    dato = read()
    #Si hay dato, si contiene algun valor
    if dato:
        #Realizamos la consulta para eliminar
        cursor.execute(f"DELETE FROM Persona WHERE id={dato[0]}")
        db.commit()
        print("**Registo eliminado correctamente**")
    cursor.close()
    db.close()

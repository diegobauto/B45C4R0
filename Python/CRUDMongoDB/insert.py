from pymongo import MongoClient

# Crear conexiones para comunicarse con Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

# Función que inserta informacion en mongo db
def insert():
    try:
        #Pedimos datos
        print("\n---- INSERTAR DATOS ----")
        id = input('Id:')
        name = input('Nombre:')
        age = input('Edad:')
        country = input('País:')

        #Insertamos los datos a la base de datos
        db.Employees.insert_one(
        {
            "id": id,
            "name": name,
            "age": age,
            "country": country
        })
        print ('Información insertada correctamente')

    except ImportError:
        platform_specific_module = None
        #print str(e)
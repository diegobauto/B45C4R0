from pymongo import MongoClient

# Crear conexiones para comunicarse con Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

# Función para actualizar registros de mongodb
def update():
    try:
        print("\n---- ACTUALIZANDO ----")
        id = input('Id:')
        name = input('Nombre:')
        age = input('Edad:')
        country = input('País:')

        #Sirve para actualizar un registro de la base de datos
        db.Employees.update_one(
        #Buscar si existe ese id en la base de datos
        {"id": id},
        {
            #Modifica los datos
            "$set": {
                "name": name,
                "age": age,
                "country": country
            }
        })
        print ("\nRegistro actualizado correctamente\n")
    except ImportError:
        platform_specific_module = None
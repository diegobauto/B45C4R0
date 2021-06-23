from pymongo import MongoClient

# Crear conexiones para comunicarse con Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


# Función para eliminar registros de mongo db
def delete():
    try:
        id = input('\nIngrese el id a eliminar:')

        #Busca el registo que contenga ese id y o elimina
        db.Employees.delete_many({"id": id})
        print('Eliminado correctamente')
        
    except ImportError:
        platform_specific_module = None
        # print str(e)

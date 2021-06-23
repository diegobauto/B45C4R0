from pymongo import MongoClient

# Crear conexiones para comunicarse con Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


# Función para leer registros de mongodb
def read():
    try:
        #Find sirve para obtener el contenido de la base de datos
        data = db.Employees.find()
        print('\n -------- BASE DE DATOS ------- \n')
        imprimir(data)

    except ImportError:
        platform_specific_module = None
        # print str(e)

def imprimir(data):
    
    print("ID\tNOMBRE\tEDAD\tPAÍS")
    for i in data:
        #print(i.get("_id"))
        print(i["id"]+"\t"+i["name"]+"\t"+i["age"]+"\t"+i["country"]+"\t")
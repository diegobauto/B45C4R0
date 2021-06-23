#Tenemos que descargar MongoDB - Community Server
#Tenemos que instalar pymongo
import insert
import update
import read
import delete

class Programa:

    def __init__(self):
        self.dato = 1

    def menu(self):
        while self.dato:
            opcion = input("\n1.Insertar\n2.Actualizar\n3.Leer\n4.Eliminar\n5.Salir\nOpción:")
            if opcion == "1":
                insert.insert()
            elif opcion == "2":
                update.update()
            elif opcion == "3":
                read.read()
            elif opcion == "4":
                delete.delete()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción Invalida") 

objeto = Programa()
objeto.menu()
import functions

print("----- Sistema CURD -----" , end="")
while (True):
    print("""
[1] Insertar Registro
[2] Ver un registro
[3] Ver todos los registros
[4] Actualizar un registro
[5] Eliminar un registro
[6] Salir""")
    opcion = input("Opción: ")
    if opcion == "1":
        functions.create()
    elif opcion == "2":
        functions.read()
    elif opcion == "3":
        functions.readAll()
    elif opcion == "4":
        functions.update()
    elif opcion == "5":
        functions.delete()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:continue
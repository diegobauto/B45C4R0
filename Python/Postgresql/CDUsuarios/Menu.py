from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

opcion = ""
while opcion!="5":
    print("\n1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Salir")
    opcion = input("Digitar opción: ")
    if opcion == "1":
        UsuarioDAO.seleccionar()
    elif opcion == "2":
        username = input("Username: ")
        password = input("Password: ")
        user = Usuario(username=username, password=password)
        UsuarioDAO.insertar(user)
    elif opcion == "3":
        id = input("Id a actualizar: ")
        username = input("Username: ")
        password = input("Password: ")
        user = Usuario(id_usuario=id, username=username, password=password)
        UsuarioDAO.actualizar(user)
    elif opcion == "4":
        id = input("Id a eliminar: ")
        user = Usuario(id_usuario=id)
        UsuarioDAO.eliminar(user)
    else:
        print("Saliendo ...")
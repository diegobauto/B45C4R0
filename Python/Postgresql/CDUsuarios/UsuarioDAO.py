from Usuario import Usuario
from CursorPool import CursorPool

class UsuarioDAO:

    _SELECCIONAR = "SELECT * FROM usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_user=%s"
    _ELIMINAR =  "DELETE FROM usuario WHERE id_user = %s"

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            print("USUARIOS".center(50,"-"))
            for i in usuarios:
                print(i)

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            print(f"\nInsertados: {cursor.rowcount}")

    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.idUsuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            print(f"\nActualizados: {cursor.rowcount}")

    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.idUsuario,)
            cursor.execute(cls._ELIMINAR, valores)
            print(f"\nEliminados: {cursor.rowcount}")
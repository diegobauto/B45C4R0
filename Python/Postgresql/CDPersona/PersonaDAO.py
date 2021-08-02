from Persona import Persona
from CursorPool import CursorPool

class PersonaDAO:

    _SELECCIONAR = "SELECT * FROM persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, emaiL=%s WHERE id_persona= %s"
    _ELIMINAR =  "DELETE FROM persona WHERE id_persona = %s"

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            for i in personas:
                print(i)

    @classmethod
    def insertar(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            return f"Insertados: {cursor.rowcount}"

    @classmethod
    def actualizar(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.idPersona)
            cursor.execute(cls._ACTUALIZAR, valores)
            return f"Actualizados: {cursor.rowcount}"

    @classmethod
    def eliminar(cls, persona):
        with CursorPool() as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR, valores)
            return f"Eliminados: {cursor.rowcount}"
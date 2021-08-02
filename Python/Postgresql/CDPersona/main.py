from Persona import Persona
from PersonaDAO import PersonaDAO

if __name__ == "__main__":
    persona1 = Persona(nombre="Juanita", apellido="Dolores", email="jdolor@email.com")
    persona2 = Persona(id_persona=21, nombre="Juana", apellido="Dolores", email="juanadlres@email.com")
    persona3 = Persona(id_persona=21)
    dao = PersonaDAO()

    #dao.seleccionar()
    #print(dao.insertar(persona1))
    #print(dao.actualizar(persona2))
    print(dao.eliminar(persona3))
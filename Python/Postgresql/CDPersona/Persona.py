class Persona:

    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self) -> str:
        return f"Id Persona: {self._id_persona}\nNombre: {self._nombre}\nApellido: {self._apellido}\nCorreo: {self._email}\n"

    @property
    def idPersona(self):
        return self._id_persona

    @idPersona.setter
    def idPersona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
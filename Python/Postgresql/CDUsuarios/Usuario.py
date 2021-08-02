class Usuario:

    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return f"Id Usuario: {self._id_usuario}, Username: {self._username}, Password: {self._password}"

    @property
    def idUsuario(self):
        return self._id_usuario

    @idUsuario.setter
    def idUsuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
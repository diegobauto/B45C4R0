from database import db

#Creamos el modelo Persona para la creación de la tabla en la base de datos
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self) -> str:
        return f"{self.id}: - {self.nombre} {self.apellido} -> {self.email}"
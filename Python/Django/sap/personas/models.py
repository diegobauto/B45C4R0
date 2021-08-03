from django.db import models
# Este archivo representa la estructura de la base de datos de nuestra aplicación
# ORM - Representacion en la base de datos

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.id} . Calle {self.calle} #{self.no_calle} - {self.pais}"

class Persona(models.Model): #Esta clase representa una tabla
    nombre = models.CharField(max_length=255) #Variable de clase, representa una columna de la base de datos
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #Creamos una llave foranea de Domicilio, y le decimos que cuando se borre un domicilio
    #el campo se pondra nulo(SET_NULL), para esto tenemos que decirle que acepte nulos(True)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    #Este metodo se ve reflejado en el servidor url:admin al momento de ver la tabla personas
    # localhost/admin
    def __str__(self) -> str:
        return f"Persona {self.id}: {self.nombre} {self.apellido} - {self.email}"
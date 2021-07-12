#No poder accerder a los atributos de nuestra clase
#Para poder hacerlo creamos los metodos get y set

class Persona():
    def __init__(self, user, nombre, apellido):
        #El guion bajo es para encapsular el atributo -> Privado
        self._user = user
        self._nombre = nombre
        self._apellido = apellido

    #Si añadimos solo el get obtendriamos un atributo de solo lectura, no podriamos 'modificarlo'
    @property
    def user(self):
        return self._user 

    #Lo comento para indicar que cuando no lo tengo habilitado
    #Marca error al momento de querer modificarlo, es un atributo de solo lectura
    """@user.setter
    def user(self, user):
        self._user = user"""
    
    #Decorador que lo que hace es que la función la tome como si fuera un atributo de nuestra clase 
    @property
    def nombre(self):
        return self._nombre

    #Debe contener el mismo nombre del property 
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apelldido(self, apellido):
        self._apelldido = apellido

persona1 = Persona("Jp","Juan", "Perez")
persona1.nombre = "Juanito"
print(persona1.nombre)

#persona1.user = "USER" marcaria error si no tengo el setter de user


#Un metodo estatico no puede acceder a las variables de instancia
#Solamente es un metodo propio de la clase

class MetodosEstaticos():

    variableClase = "Mi variable propia de la clase"

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    #Un metodo estatico no puede acceder a las variable de instancia
    @staticmethod
    def metodoEstatico():
        return MetodosEstaticos.variableClase

#Accediendo al método estatico
print(MetodosEstaticos.metodoEstatico())
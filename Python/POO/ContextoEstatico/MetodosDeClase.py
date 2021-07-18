#staticmethod y classmethod se asocian a la clase en si misma
#Contexto Dinamico(Instancias u objetos) puede acceder al contexto Estatico(static o de clase)

class MetodosDeClase():

    variableClase = "Mi variable propia de la clase"

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    #Un metodo estatico no puede acceder a las variable de instancia
    @staticmethod
    def metodoEstatico():
        #print(self.variableInstancia) 
        return MetodosDeClase.variableClase

    #Metodo de la clase, recibe una referencia que es nuestra propia clase
    #Accediendo a las variables de clase o metodos de clase
    @classmethod
    def metodoClase(cls):
        return cls.variableClase

    #Podemos acceder destre un metodo de Instancia a un metodo de clase o estatico
    #Tambien podemos acceder a las variables de clase y de instancia
    def metodoInstancia(self):        
        print(self.variableClase)
        print(self.variableInstancia)
        return self.metodoClase() + " - " + self.metodoEstatico()

#Accediendo al método de clase
print(MetodosDeClase.metodoClase())

#Puedo acceder tambien a traves de un objeto
objeto = MetodosDeClase("Variable de Instancia")
print(objeto.metodoClase())
print(objeto.metodoInstancia())

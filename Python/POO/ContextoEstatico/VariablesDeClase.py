#La variable se va a compartir con todos los objetos, cualquier objeto que quiera acceder o modificar
#va a ver la misma información


class VariableDeClase:
    variableClase = "Esta es la variable propia de la clase"

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

#Imprimimos nuestra variable propia de la clase
print(VariableDeClase.variableClase)

objeto1 = VariableDeClase("Objeto1: Varible de Instancia")
print(objeto1.variableInstancia)
print(objeto1.variableClase) #Podemos acceder a la variable de la clase ppr medio de un objeto

""" Puedo crear variables de clase al vuelo(En cualquier momento) """
VariableDeClase.variableClase2 = "Esta es la variable propia de la clase 2"

objeto2 = VariableDeClase("Objeto2: Variable de Instancia")
print(objeto2.variableInstancia)
print(objeto2.variableClase) #Vemos que compartimos la misma variable de clase en ambos objetos

print(VariableDeClase.variableClase2)
print(objeto1.variableClase2) 
print(objeto2.variableClase2) 
    
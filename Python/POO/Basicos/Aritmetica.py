class Aritmetica:
    #Atributos de nuestra clase

    def __init__(self, num1, num2):
        #Atributos de nuestros objetos
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2
    
aritmetica1 = Aritmetica(5,3)
print(aritmetica1.dividir())

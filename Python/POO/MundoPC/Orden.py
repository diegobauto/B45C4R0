class Orden():

    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras #lista de computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)        

    def __str__(self):
        computadorasStr = "\n"
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__() + "\n"
        return f"Orden #{self.idOrden}: {computadorasStr}"

    @property
    def idOrden(self):
        return self._idOrden
    
    @idOrden.setter
    def idOrden(self, idOrden):
        self._idOrden = idOrden

    @property
    def computadoras(self):
        return self._computadoras
    
    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras
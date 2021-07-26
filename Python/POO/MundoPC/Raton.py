from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contadorRatones = 0

    def __init__(self, marca, tipoEntrada):
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f"Raton #{self._idRaton}: {self.marca} - {self.tipoEntrada}"
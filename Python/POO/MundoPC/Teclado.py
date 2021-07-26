from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contadorTeclados = 0

    def __init__(self, marca, tipoEntrada):
        Teclado.contadorTeclados += 1
        self._idTeclado = Teclado.contadorTeclados
        super().__init__(marca, tipoEntrada)

    def __str__(self):
        return f"Teclado #{self._idTeclado}: {self.marca} - {self.tipoEntrada}"
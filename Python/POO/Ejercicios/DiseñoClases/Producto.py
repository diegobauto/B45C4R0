class Producto:

    contadorProductos = 0

    def __init__(self, nombre, precio):
        Producto.contadorProductos += 1
        self._idProducto = Producto.contadorProductos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f"{self._idProducto}, {self._nombre}, {self._precio}"
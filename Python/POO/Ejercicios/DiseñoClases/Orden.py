class Orden:

    contadorOrdenes = 0

    def __init__(self, productos):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = []
        for producto in self._productos:
            productos_str.append([producto.__str__()])
        return f"Orden #{self._idOrden} --> Productos: {productos_str}"
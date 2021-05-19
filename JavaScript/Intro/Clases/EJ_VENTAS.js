class Producto{

    static contadorProductos = 1;

    constructor(nombre, precio){
        this.nombre = nombre;
        this.precio = precio;
        this.idProducto = Producto.contadorProductos++;
    }

    get getIdProducto(){
        return this.idProducto;
    }

    get getNombre(){
        return this.nombre;
    }

    set setNombre(nombre){
        this.nombre = nombre;
    }

    get getPrecio(){
        return this.precio;
    }

    set setPrecio(precio){
        this.precio = precio;
    }

    toString(){
        return `IdProducto: ${this.idProducto}\nNombre: ${this.nombre}\nPrecio: $${this.precio}`;
    }
}

class Orden{

    static contadorOrdenes = 1;

    static get MaxProductos(){
        return 5;
    }

    constructor(){
        this.productos = [];
        this.idOrden = Orden.contadorOrdenes++;
    }

    get getIdOrden(){
        return this.idOrden;
    }

    agregarProducto(producto){
        if (this.productos.length < Orden.MaxProductos) {
            this.productos.push(producto);
        } else {
            console.log("No se pueden agraegar más productos");
        }
    }

    calcularTotal(){
        let total = 0;
        for (let producto of this.productos) {
            total += producto.precio;
        }
        return "$" + total;
    }

    mostrarOrden(){
        let productosOrden = "";
        for (let producto of this.productos){
            productosOrden += producto.toString() + "\n\n";
        }
        console.log(`Orden #${this.idOrden} \nProductos: \n\n${productosOrden}Total: ${this.calcularTotal()}`);
    }
}

let producto1 = new Producto("Lapiz", 1800);
let producto2 = new Producto("Borrador", 800);
let producto3 = new Producto("Tajalapiz", 600);
let producto4 = new Producto("Esfero", 1200);
let producto5 = new Producto("Marcador", 2000);
let producto6 = new Producto("Block", 2500);

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto4);
orden1.agregarProducto(producto5);
orden1.agregarProducto(producto6);

orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarProducto(producto4);
orden2.agregarProducto(producto6);

orden2.mostrarOrden();
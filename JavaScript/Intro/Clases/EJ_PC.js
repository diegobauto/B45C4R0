class DispositivoEntrada{
    constructor(tipoEntrada, marca){
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }

    get getTipoEntrada(){
        return this.tipoEntrada;
    }

    set setTipoEntrada(tipoEntrada){
        this.tipoEntrada = tipoEntrada;
    }

    get getMarca(){
        return this.marca;
    }

    set setMarca(marca){
        this.marca = marca;
    }
}

class Raton extends DispositivoEntrada{
    static contadorRatones = 1;

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca);
        this.idRaton = Raton.contadorRatones++;
    }

    get getIdRaton(){
        return this.idRaton;
    }

    toString(){
        return this.idRaton + " " + this.tipoEntrada + " " + this.marca;
    }
}

class Teclado extends DispositivoEntrada{
    static contadorTeclados = 1;

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca);
        this.idTeclado = Teclado.contadorTeclados++;
    }

    get getIdTeclado(){
        return this.idTeclado;
    }

    toString(){
        return this.idTeclado + " " + this.tipoEntrada + " " + this.marca;
    }
}

class Monitor{
    static contadorMonitores = 1;

    constructor(marca, tamaño){
        this.marca = marca;
        this.tamaño = tamaño;
        this.idMonitor = Monitor.contadorMonitores++;
    }

    get getIdMonitor(){
        return this.idMonitor;
    }

    get getMarca(){
        return this.marca
    }

    set setMarca(marca){
        this.marca = marca;
    }

    get getTamaño(){
        return this.tamaño
    }

    set setTamaño(tamaño){
        this.tamaño = tamaño;
    }

    toString(){
        return this.idMonitor + " " + this.marca + " " + this.tamaño;
    }
}

class Computadora{
    static contadorComputadoras = 1;

    constructor(nombre, monitor, raton, teclado){
        this.nombre = nombre;
        this.monitor = monitor;
        this.raton = raton;
        this.teclado = teclado;
        this.idComputadora = Computadora.contadorComputadoras++;
    }

    get getNombre(){
        return this.nombre;
    }

    set setNombre(nombre){
        this.nombre = nombre;
    }

    toString(){
        return `Computadora ${this.idComputadora}:
        Nombre: ${this.nombre}
        Monitor: ${this.monitor}
        Raton: ${this.raton}
        Teclado: ${this.teclado}`; 
    }
}

class Orden{
    static contadorOrdenes = 1;

    constructor(){
        this.computadoras = [];
        this.idOrden = Orden.contadorOrdenes++;
    }

    get getIdOrden(){
        return this.idOrden;
    }

    agregarComputadora(computadora){
        this.computadoras.push(computadora);
    }

    mostrarOrden(){
        let computadorasOrden = "";
        for (let i of this.computadoras){
            computadorasOrden += i.toString() + "\n\n";
        }
        console.log(`ORDEN #${this.idOrden} \nComputadoras: \n\n${computadorasOrden}`);
    }
}

let monitor1 = new Monitor("ASUS", "15.6");
let raton1 = new Raton("USB","HP");
let teclado1 = new Teclado("USB", "MSI");

let computadora1 = new Computadora("HP", monitor1, raton1, teclado1);
let computadora2 = new Computadora("Armada", monitor1, raton1, teclado1);

//Creamos una orden
let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.mostrarOrden();

//Creamos una segunda orden
let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.mostrarOrden();
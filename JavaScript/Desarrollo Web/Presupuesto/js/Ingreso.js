class Ingreso extends Dato{

    static contadorIngreso = 1;

    constructor(descripcion, valor){
        super(descripcion, valor);
        this.idIngreso = Ingreso.contadorIngreso++;
    }

    get getIdIngreso(){
        return this.idIngreso;
    }
}
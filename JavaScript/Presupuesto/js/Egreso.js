class Egreso extends Dato{

    static contadorEgreso = 1;

    constructor(descripcion, valor){
        super(descripcion, valor);
        this.idEgreso = Egreso.contadorEgreso++;
    }

    get getIdEgreso(){
        return this.idEgreso;
    }
}
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    get getNombre(){
        return this.nombre;
    }

    set setNombre(nombre){
        this.nombre = nombre;
    }

    get getApellido(){
        return this.apellido;
    }

    set setApellido(apellido){
        this.apellido = apellido;
    }

    nombreCompleto(){
        return this.nombre + " " + this.apellido;
    }
}

class Empleado extends Persona{
    constructor(nombre, apellido, departemento){
        super(nombre, apellido); //Llamar al constructor de la clase padre
        this.departemento = departemento;
    }

    get getDepartamento(){
        return this.departemento;
    }

    set setDepartamento(departemento){
        this.departemento = departemento;
    }

    //Sobreescritura
    //Es sobreescribir el metodo nombreCompleto() de la clase padre, añadiendo de más
    nombreCompleto(){
        return super.nombreCompleto() + " , " + this.departemento;
    }
}

let empleado1 = new Empleado("Juan","Perez","Sistemas");
console.log(empleado1.nombreCompleto());

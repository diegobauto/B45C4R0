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

    //Polimorfismo
    //Hacer la misma funcion pero de diferente manera
    toString(){
        return this.nombreCompleto();
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

    nombreCompleto(){
        return super.nombreCompleto() + " , " + this.departemento;
    }
}

//Todos muestran el nombre Completo (toString) pero cada clase de diferente forma
let persona1 = new Persona("Ana", "Ruiz");
console.log(persona1.toString());

let empleado1 = new Empleado("Juan","Perez","Sistemas");
console.log(empleado1.toString());

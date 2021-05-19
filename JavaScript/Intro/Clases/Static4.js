//Ejercicio
class Persona{

    static contador = 0;

    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
        this.id = ++Persona.contador;
    }

    nombreCompleto(){
        return this.id + " - " + this.nombre + " " + this.apellido;
    }

    toString(){
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{
    constructor(nombre, apellido, area){
        super(nombre, apellido);
        this.area = area;
    }

    nombreCompleto(){
        return super.nombreCompleto() + " , " + this.area;
    }
}

let persona1 = new Persona("Ana", "Ruiz");
console.log(persona1.toString());

let empleado1 = new Empleado("Juan","Perez","Sistemas");
console.log(empleado1.toString());


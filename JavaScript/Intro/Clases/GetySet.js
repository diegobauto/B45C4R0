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
}

let persona1 = new Persona("Juan","Perez");
console.log(persona1.getNombre);

persona1.setNombre = "Pepito";
console.log(persona1.getNombre);
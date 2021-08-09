class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    get getNombre(){
        return this.nombre
    }

    set setNombre(nombre){
        this.nombre = nombre;
    }

    get getApellido(){
        return this.apellido
    }

    set setApellido(apellido){
        this.apellido = apellido;
    }

    mostratDatos(){
        return this.nombre + " " + this.apellido;
    }
}
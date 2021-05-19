class Persona{

    static contadorPersonas = 1;

    constructor(nombre, apellido, edad){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.idPersona = Persona.contadorPersonas++;
    }

    get getIdPersona(){
        return this.idPersona
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

    get getEdad(){
        return this.edad;
    }

    set setEdad(edad){
        this.edad = edad;
    }

    toString(){
        return "P" + this.idPersona + " - " +this.nombre + " " + this.apellido + " " + this.edad;
    }
}

//EMPLEADO
class Empleado extends Persona{

    static contadorEmpleados = 1;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this.sueldo = sueldo;
        this.idEmpleado = Empleado.contadorEmpleados++;
    }

    get getIdEmpleado(){
        return idEmpleado;
    }

    get getSueldo(){
        return this.sueldo;
    }

    set setSueldo(sueldo){
        this.sueldo = sueldo;
    }

    toString(){
        return super.toString() + " $" + this.sueldo + " - E"+ this.idEmpleado ;
    }
}

class Cliente extends Persona{

    static contadorClientes = 1;

    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this.fechaRegistro = fechaRegistro;
        this.idCliente = Cliente.contadorClientes++;
    }

    get getIdCliente(){
        return this.idCliente;
    }

    get getFechaRegistro(){
        return this.fechaRegistro;
    }

    set setFechaRegistro(fechaRegistro){
        this.fechaRegistro = fechaRegistro;
    }

    toString(){
        return super.toString() + " " + this.fechaRegistro + " - C" + this.idCliente;
    }
}

//Prueba clase Persona
let persona1 = new Persona("Juan", "Perez", 54);
console.log(persona1.toString());

let persona2 = new Persona("Ana", "Rodriguez", 28);
console.log(persona2.toString());

let empleado1 = new Empleado("Rodrigo", "Gonzales", 19, 6800)
console.log(empleado1.toString());

let empleado2 = new Empleado("Santiago", "Quintero", 23, 5800)
console.log(empleado2.toString());

let cliente1 = new Cliente("Jaime", "Cervantes", 40, new Date());
console.log(cliente1.toString());

let cliente2 = new Cliente("Lola", "Peranta", 43, new Date());
console.log(cliente2.toString());
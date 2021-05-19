class Empleado{
    constructor(nombre, sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: \nNombre: ${this.nombre}, Sueldo ${this.sueldo}`;
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo);
        this.departamento = departamento;
    }

    //Sobreescribiendo el metodo de la clase padre(Empleado)
    obtenerDetalles(){
        return `Gerente: \n${super.obtenerDetalles()} Depto: ${this.departamento}`;
    }
}


//POLIMORFISMO
function imprimir(tipo) {
    console.log(tipo.obtenerDetalles());
}

let empleado1 = new Empleado("Juan", 600);
console.log(empleado1.obtenerDetalles());

let gerente1 = new Gerente("Carlos", 5000, "Sistemas");
console.log(gerente1.obtenerDetalles());

imprimir(empleado1);
imprimir(gerente1);

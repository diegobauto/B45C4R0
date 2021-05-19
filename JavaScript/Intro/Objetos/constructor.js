//Constructor de objetos de tipo Persona
function Persona(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function() {
        return this.nombre + " " + this.apellido
    }
}

let estudiante = new Persona("Juan", "Perez", "nose@gmail.com");
console.log(estudiante);

let profesor = new Persona("Alberto", "Gonzales", "nose@gmail.com")
console.log(profesor);

profesor.email = "otronose@gmail.com"

console.log(profesor);
console.log(profesor.nombreCompleto());
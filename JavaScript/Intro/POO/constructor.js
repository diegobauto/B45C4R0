//Constructor de objetos de tipo Persona
function Persona(nombre, apellido, email) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
}

let estudiante = new Persona("Juan", "Perez", "nose@gmail.com");
console.log(estudiante);
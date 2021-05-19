function Persona(nombre, apellido) {
    this.nomre = nombre;
    this.apellidof = apellido;
}

Persona.prototype.email = "nose@gmail.com";

let padre = new Persona("Juan", "Perez");
padre.email = "padre@gmail.com";
console.log(padre.email);

let madre = new Persona("Ana", "Perez");
console.log(madre.email);
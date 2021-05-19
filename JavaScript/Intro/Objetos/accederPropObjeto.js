//ACCEDER A LAS PROPIEDADES/ATRIBUTOS DE UN OBJETO

//Clase persona
let persona = {
    nombre: "Diego",
    apellido: "Bautista",
    edad: 20,
    //Metodos
    nombreCompleto: function() {
        return this.nombre+" "+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona["nombre"]);

for (nombrePropiedad in persona) {
    console.log(nombrePropiedad);
    console.log(persona[nombrePropiedad]);
}

let personaArray = Object.values(persona);
console.log(personaArray);

let personaJson = JSON.stringify(persona);
console.log(personaJson);
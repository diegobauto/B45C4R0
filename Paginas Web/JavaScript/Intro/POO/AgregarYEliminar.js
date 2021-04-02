/*
AGREGAR Y ELIMINAR PROPIEDADES/ATRIBUTOS DE UN OBJETO
*/

let persona = {
    nombre: "Diego",
    apellido: "Bautista",
    edad: 20,
    //Metodos
    nombreCompleto: function() {
        return this.nombre+" "+this.apellido;
    }
}

//Agregar
persona.tel = 123457;
console.log(persona);

//Eliminar
delete persona.tel;
console.log(persona);
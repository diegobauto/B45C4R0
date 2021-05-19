//Pasarle argumentos a la funcion Call
let persona1 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto: function (tel, email) {
        return this.nombre + " " +this.apellido+", "+tel+" - "+email;
    }
}

let persona2 = {
    nombre: "Ana",
    apellido: "Lara"
}

//Uso de call para usar el metodo nombreCompleto de persona1 en persona2 con argumentos 
console.log(persona1.nombreCompleto.call(persona2, 44558899, "nose@gmail.com"));
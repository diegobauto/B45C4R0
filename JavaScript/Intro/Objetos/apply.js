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

//Uso de aply para usar el metodo nombreCompleto
//de persona1 en persona2 con argumentos
let arreglo = [44558899, "nose@gmail.com"]
console.log(persona1.nombreCompleto.apply(persona2, arreglo));
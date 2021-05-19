let persona1 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto: function () {
        return this.nombre + " " +this.apellido;
    }
}

let persona2 = {
    nombre: "Ana",
    apellido: "Lara"
}

console.log(persona1.nombreCompleto());
//Uso de call para usar el metodo nombreCompleto de persona1 en persona2
console.log(persona1.nombreCompleto.call(persona2));
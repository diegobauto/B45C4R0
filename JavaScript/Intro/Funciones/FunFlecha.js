function miFuncion() {
    console.log("Saludos");
}

//No se aplica el hoisting
let miFuncion2 = function(){
    console.log("Saludo numero 2");
}

//No se aplica el hoisting
let funcionFlecha = () => {
    console.log("Saludos desde mi función flecha");
}

let funcionFlecha2 = () => console.log("Saludos desde mi función flecha");
let saludar = () => "Saludos";
let regresaObjeto = () => ({ "nombre" : "Juan"})
let parametros = (parametro) => console.log(parametro);

funcionFlecha();
funcionFlecha2();
console.log(saludar());
console.log(regresaObjeto());
parametros("Hola");


//La variables son dinamicas, No definimos el tipo de la variable
var nombre = "Juan";//Variable de tipo String
var numero = 98;//Variable de tipo entero
var objeto = {nombre: "Alberto",edad: 45,};//Variable de tipo Objeto
var simbolo = Symbol("mi Simbolo");//Tipo de dato Simbolo
console.log(objeto);
console.log(typeof objeto);
console.log(typeof numero);
console.log(typeof simbolo);

//************************* ARREGLOS ***********************
const nombres = ['Diego','Juan','Pepito'];
console.log(nombres);
console.log(nombres[0]);

nombres.forEach(element => {
    console.log(element);
});

//Modificar un valor
nombres[0] = "Alejandro";
console.log(nombres[0]);

//Agregar mas elementos
nombres.push("Oscar");
console.log(nombres);

//Preguntar si es un arreglo
console.log(Array.isArray(nombres));
console.log(nombres instanceof Array);
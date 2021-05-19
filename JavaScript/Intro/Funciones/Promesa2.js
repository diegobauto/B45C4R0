//Uso de setTimeout y promesa
//Asincrono, que se ejecuta todo a la vez, no es lineal
let promesa = new Promise( resolver => {
    setTimeout(() => resolver("Saludos"), 3000);
} );
promesa.then(valor => console.log(valor));

//Async
//Podemos pasar una función a promesa solamente con el async
async function miFuncionconPromesa() {
    return "Saludos con promesa y async";
}
miFuncionconPromesa().then(valor => console.log(valor));

//Await y Aync
//Await solo se puede usar dentro de una funcion con Async
async function miFuncionAyA() {
    let miPromesa = new Promise( resolver => {
        resolver("Promesa - Await y Async");
    });
    console.log(await miPromesa);
}
miFuncionAyA();

async function funcionAwaitAsyncTimeout() {
    console.log("Inicio");
    let miPromesa1 = new Promise( resolver => {
        setTimeout(() => resolver("Promesa con Await y Timeout"), 3000);
    });
    console.log(await miPromesa1);
    console.log("Fin");
}
funcionAwaitAsyncTimeout();
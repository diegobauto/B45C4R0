//LLAMAR A UNA FUNCION DENTRO DE OTRA FUNCION, PASANDOLA COMO ARGUMENTO
function imprimir(mensaje) {
    console.log("Resultado: " + mensaje);
}

function sumar(n1, n2, functionCallback) {
    let total = n1+n2;  
    functionCallback(total);
}
sumar(5,3,imprimir);

//LLamada asíncronas con uso setTimeout
//Realiza una acción despues de cierto tiempo ( una vez )
function funcionCallback() {
    console.log("Saludo asincrono despues de 3s");
}
setTimeout(funcionCallback, 3000);//Despues de tres segundos
setTimeout( () => console.log("Saludo de 4s"), 4000); //Función flecha

//LLamada asíncronas con uso setInterval
//Realiza una accion cada cierto tiempo ( varias veces )    
let reloj = () => {
    let fecha = new Date();
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}
setInterval(reloj, 1000); //1s
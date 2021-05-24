"use strict";
var texto = "Hola desde TypeScript";
//Solo puedo cambiar el tipo de alguna variable con any 
var cualquiera;
cualquiera = "2";
cualquiera = 5;
function saludar() {
    console.log(texto);
    console.log(cualquiera);
}
saludar();

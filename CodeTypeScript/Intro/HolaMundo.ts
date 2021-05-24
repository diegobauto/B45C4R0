let texto = "Hola desde TypeScript";

//Solo puedo cambiar el tipo de alguna variable con any 
let cualquiera:any;
cualquiera = "2";
cualquiera = 5;


function saludar() {
    console.log(texto);
    console.log(cualquiera);
}

saludar();
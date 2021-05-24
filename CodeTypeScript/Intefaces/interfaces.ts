interface Usuario{
    nombre:string;
    password:string;
    //Atributo opcional con ?
    confirmarPassword?:string;
}

let usuario:Usuario = {nombre: "Juan", password:"1234"};
console.log(usuario);
console.log(usuario.nombre);


interface Abordar{
    abordarTransporte():void;
}

let avion:Abordar = {
    abordarTransporte: function() {
        console.log("abordando");
        
    }
}
console.log(avion.abordarTransporte());
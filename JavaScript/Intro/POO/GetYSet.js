/*
METODO GET Y SET
*/

let persona = {
    nombre: "Diego",
    apellido: "Bautista",
    edad: 20,
    animal: "perro",
    //Metodos
    get nombreCompleto() {
        return this.nombre+" "+this.apellido;
    },

    get metodoAnimal(){
        return this.animal.toUpperCase();
    },
    set metodoAnimal( otroAnimal ){
        this.animal = otroAnimal.toUpperCase();
    }
}

//Llama al metodo set
console.log(persona.nombreCompleto);
console.log(persona.metodoAnimal);

//Llama el metodo set
persona.metodoAnimal = "gato";
console.log(persona.metodoAnimal);
//Se almaceno correctamente el valor 
console.log(persona.animal);


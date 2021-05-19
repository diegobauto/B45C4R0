//CONSTANTES ESTATICAS - Ejercicio
class Persona{

    static contador = 1;

    static get max(){
        return 3;
    }

    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
        //Si nos pasamos de el limite de nuestra constante (3)
        if(Persona.contador < Persona.max){
            this.id = Persona.contador++;
        }
        else{
            console.log("Se supero al limite de objetos");
        }
    }

    completo(){
        return this.id + " - " + this.nombre + " " + this.apellido;
    }
}

class Empleado extends Persona{
    constructor(nombre, apellido){
        super(nombre, apellido);
    }
}

//No podemos cambiar el atributo
console.log(Persona.max);
Persona.max = 10;
console.log(Persona.max);

let persona1 = new Persona("Ana", "Ruiz");
console.log(persona1.completo());
let empleado1 = new Empleado("Juan","Perez");
console.log(empleado1.completo());
//Al crear otro objeto nos pasamos del limite 
let persona2 = new Persona("Lola", "Ramirez"); 
//Esta sin definir ya que no fue asignado
console.log(persona2.completo());
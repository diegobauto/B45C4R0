//ATRIBUTOS ESTÁTICOS 
//LOS METODOS Y ATRIBUTOS ESTATICOS SE HEREDAN A LAS CLASES HIJAS
class Persona{
    static edad = 0;

    constructor(){
        Persona.edad++;
    }
}

class Empleado extends Persona{

}

//Como es estatica toca llamarla desde una clase
let persona1 = new Persona;
console.log(Persona.edad);

let empleado1 = new Empleado;
console.log(Empleado.edad);

console.log(Persona.edad);
console.log(Empleado.edad);
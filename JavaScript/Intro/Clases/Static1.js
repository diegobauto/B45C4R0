//METODOS ESTÁTICOS
class Persona{
    constructor(nombre){
        this.nombre = nombre;
    }

    static saludar(){
        console.log("Saludos desde el metodo static");
    }

    //Para pasarle un parametro de tipo objeto
    static saludar2(persona){
        console.log("Hola " + persona.nombre);
    }
}

//No es posible llamar un metodo statico desde un obejto
//Un metodo static solo se puede llamar desde la clase
Persona.saludar();

let persona2 = new Persona("Juan");
Persona.saludar2(persona2);
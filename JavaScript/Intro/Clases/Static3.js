//ATRIBUTOS NORMALES Y ESTATICOS

class Persona{
    static codigo = "EE48";//Atributo de la clase
    email = "Email por Default"; //atributo de los objetos 
}

let persona1 = new Persona();
//LLamamos a nuestro atributo
console.log(persona1.email);

//Es como si se estuviera creando un nuevo atributo y se asocia a nuestro objeto
//Es un nuveo valor, por eso se marca como que no esta definifido
console.log(persona1.codigo);

//Es como si se estuviera creando un nuevo atributo y se asocia a nuestra clase
//Es un nuveo valor, por eso se marca como que no esta definifido
console.log(Persona.email);

//SOLO PUEDO ACCEDER A LOS ATRIBUTOS ESTATICOS POR MEDIO DE LA CLASE
//SOLO PUEDO ACCEDER A LOS OBJETOS NORMALES POR MEDIO DE UN OBJETO
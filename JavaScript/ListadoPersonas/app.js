const personas = [
    new Persona("Juan", "Perez"),
    new Persona("Ana", "Perez")
];

function agregarPersona() {
    const form = document.getElementById("form");
    let nombre = form["nombre"].value;
    let apellido =form["apellido"].value;
    if (nombre != "" && apellido != "") {
        personas.push(new Persona(nombre, apellido));
        console.log(personas);
        mostrarPersonas();
    } else {
        alert("Falta algun campo por ingresar");
    }
    
}

function mostrarPersonas() {    
    let textPersonas = "";
    for (let i of personas) {
        textPersonas += "<li>"+i.mostratDatos()+"</li>";
    }
    document.getElementById("personas").innerHTML = textPersonas;
}
let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = true;
    if(expresion)
        resolver("Todo correcto");
    else
        rechazar("Error");
});

//Le pasamos dos funciones flecha a nuestra Promesa
miPromesa.then( 
    Correcto => console.log(Correcto), 
    Incorrecto => console.log(Incorrecto)
);

//Otra forma pero con el catch
miPromesa
.then( Correcto => console.log(Correcto))
.catch(Incorrecto => console.log(Incorrecto));
proyectos = {
    1: {
        "name": "Candy Crush", 
        "des": "Juego de Candy Crush realizado con su interfaz grafica",
        "len": "JAVA",
        "img":"https://k1.midasplayer.com/images/share/banners/candycrush.png?_v=kmoqjd"
    },
    2: {
        "name": "Ingresos y Egresos", 
        "des": "Sistema de ingresos y egresos, para manejar inventarios", 
        "len": "HTML / CSS / JAVASCRIPT" ,
        "img":"https://economipedia.com/wp-content/uploads/ingreso-y-egreso.jpg"
    },
    3: {
        "name": "Candy Crush", 
        "des": "Juego de Candy Crush realizado con su interfaz grafica",
        "len": "JAVA",
        "img":"https://k1.midasplayer.com/images/share/banners/candycrush.png?_v=kmoqjd"
    },
    4: {
        "name": "Ingresos y Egresos", 
        "des": "Sistema de ingresos y egresos, para manejar inventarios", 
        "len": "HTML / CSS / JAVASCRIPT" ,
        "img":"https://economipedia.com/wp-content/uploads/ingreso-y-egreso.jpg"
    },
    5: {
        "name": "Candy Crush", 
        "des": "Juego de Candy Crush realizado con su interfaz grafica",
        "len": "JAVA",
        "img":"https://k1.midasplayer.com/images/share/banners/candycrush.png?_v=kmoqjd"
    },
}


let cargar = () =>{
    cargarTarjetas()
}

const crearTarjeta = (titulo, des, len, imagen) => {
    let card = `
    <div class="card">
        <img src="${imagen}" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title">${titulo}</h5>
            <p class="card-text">${des}</p>
            <p class="card-text lenguaje">${len}</p>
            <a href="#" class="btn btn-primary">Ir al repositorio</a>
        </div>
    </div>`
    return card;
};

const cargarTarjetas = () => {
    let tarjetas = "";
    for (let i in proyectos) {
        tarjetas += crearTarjeta(proyectos[i].name, proyectos[i].des, proyectos[i].len, proyectos[i].img);
    }
    document.getElementById("tarjetas").innerHTML = tarjetas;
}
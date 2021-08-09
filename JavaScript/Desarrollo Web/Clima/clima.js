let soleado = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Nuages.gif/334px-Nuages.gif"
let lluvioso = "https://pa1.narvii.com/6483/0da88e7eed6d66b02a5587f6655608ab01491896_hq.gif"
let nublado = "https://thumbs.gfycat.com/AnchoredEcstaticAtlanticspadefish-size_restricted.gif"

window.onload = () => {
    cargarAPI("Bogotá", "CO")
}

const buscar = () => {
    ciudad = document.getElementById("ciudad").value;
    data = cargarAPI(ciudad);
    console.log(data);
}

const cargarAPI = (lugar, country) => {
    const API = "0893a84e0737f4117e1abd6a42b8dce3";
    const url = `http://api.openweathermap.org/data/2.5/weather?q=${lugar},${country}&appid=${API}&units=metric&lang=sp`
    fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        obtenerFecha(data);
        asignarValores(data);
    })
}

const obtenerFecha = (data) => {
    let dateSpanish = new Date(data.dt*1000).toLocaleString("es-ES",{
        timeStyle:"short",
        dateStyle:"long"
    });
    return dateSpanish;
}

const asignarValores = (data) => {
    document.getElementById("lugar").innerHTML = data.name + ", " + data.sys.country;
    document.getElementById("descripcion").innerHTML = data.weather[0].description;
    document.getElementById("icono").src = `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`;
    document.getElementById("hora").innerHTML = obtenerFecha(data);
    document.getElementById("grados").innerHTML = Math.round(data.main.temp) + "<div class=c> °C</div>" ;
    body = document.getElementById("body");
    if(Math.round(data.main.temp) > 20){
        body.style.backgroundImage = `url(${soleado})`;
    }
    else{
        body.style.backgroundImage = `url(${nublado})`;
    }
}


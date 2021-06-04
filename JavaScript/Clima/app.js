window.onload = () => {
    cargarAPI("Colombia")
}

const buscar = () => {
    ciudad = document.getElementById("ciudad").value;
    cargarAPI(ciudad);    
}

const cargarAPI = async (lugar) => {
    //Realizamos la consulta a la API
    const res = await fetch(`https://community-open-weather-map.p.rapidapi.com/find?q=${lugar}&units=metric&lang=sp`, {
	"method": "GET",
	"headers": {
		"x-rapidapi-key": "0d49ab5ce8msh64caccb819cdb7cp1d2e2djsn4753bc0748e3",
		"x-rapidapi-host": "community-open-weather-map.p.rapidapi.com"
	}});
    const data = await res.json();

    obtenerFecha(data);
    asignarValores(data);   
}

const obtenerFecha = (data) => {
    console.log(data.list[data.list.length-1]);
    let dateSpanish = new Date(data.list[data.list.length-1].dt*1000).toLocaleString("es-ES",{
        timeStyle:"short",
        dateStyle:"long"
    });
    return dateSpanish;
}

const asignarValores = (data) => {
    document.getElementById("city").innerHTML = data.list[0].name;
    document.getElementById("descripcion").innerHTML = data.list[0].weather[0].description;
    document.getElementById("icono").src = `http://openweathermap.org/img/wn/${data.list[0].weather[0].icon}.png`;
    document.getElementById("hora").innerHTML = obtenerFecha(data);
    document.getElementById("grados").innerHTML = data.list[0].main.temp + "°C";
}
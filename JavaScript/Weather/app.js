const country = "london";
const API = "0893a84e0737f4117e1abd6a42b8dce3";
const url = `http://api.openweathermap.org/data/2.5/weather?q=${country}&appid=${API}`

fetch(url)
.then(response => response.json())
.then(data => {
    console.log("Objeto:",data);
})
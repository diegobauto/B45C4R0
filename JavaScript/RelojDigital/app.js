let reloj = () => {
    let reloj = new Date();
    let hora = formatoHora(reloj.getHours());
    let minutos = formatoHora(reloj.getMinutes());
    let segundos = formatoHora(reloj.getSeconds());
    document.getElementById("hora").innerHTML = (`${hora}:${minutos}:${segundos}`);

    const meses = ["En", "Febr", "Mzo", "Abr", "May", "Jun", "Jul", "Agt", "Sept", "Oct", "Nov", "Dic"];
    const dias = ["Dom", "Lunes", "Mar", "Mie", "Jue", "Vie", "Sab"];

    let diaSemana = dias[reloj.getDay()];
    let dia = reloj.getDate();
    let mes = meses[reloj.getMonth()];
    let año = reloj.getFullYear();
    document.getElementById("fecha").innerHTML = (`${diaSemana}, ${dia} de ${mes} del ${año}`);

    //Toogle lo que hace es que si esta aplicado el estilo lo agrega, de lo contrario lo quita
    document.getElementById("contenedor").classList.toggle("animar");
}

const formatoHora = (hora) => {
    if(hora<10){
        hora = "0"+hora;
    }
    return hora;
}


setInterval(reloj, 1000);

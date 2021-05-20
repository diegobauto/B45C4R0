function sumar() {
    const formulario = document.getElementById("formulario");
    let resultado = document.getElementById("resultado");
    n1 = formulario["n1"].value;
    n2 = formulario["n2"].value;
    let total = parseInt(n1)+parseInt(n2);
    if(isNaN(total))
        total = "Falta ingresar algún campo";
    resultado.innerHTML = "Resultado: " + total;
}
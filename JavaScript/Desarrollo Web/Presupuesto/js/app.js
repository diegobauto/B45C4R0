const ingresos = [
    new Ingreso("Salario", 2000),
    new Ingreso("Venta", 2000)
];

const egresos = [
    new Egreso("Descuento", 200),
    new Egreso("Compra", 300)
];


let cargarApp = () => {
    cargarIngresos();
    cargarEgresos();
    cargarCabecero();
}

let totalIngresos = () => {
    let totalIngresos = 0;
    for (let i of ingresos) {
        totalIngresos += i.valor;
    }
    return totalIngresos;
}

let totalEgresos = () => {
    let totalEgresos = 0;
    for (let i of egresos) {
        totalEgresos += i.valor;
    }
    return totalEgresos;
}


let cargarCabecero = () => {
    let presupuesto = totalIngresos() - totalEgresos();
    let porcentajeEgreso = totalEgresos()/totalIngresos();
    document.getElementById("presupuesto").innerHTML = formatoMoneda(presupuesto);
    document.getElementById("ingreso").innerHTML = formatoMoneda(totalIngresos());
    document.getElementById("egreso").innerHTML = formatoMoneda(totalEgresos());
    document.getElementById("egresoPorcentaje").innerHTML = formatoPorcentaje(porcentajeEgreso);
}

const formatoMoneda = (valor) => {
    return valor.toLocaleString("en-US", {style:"currency", currency:"USD", minimumFractionDigits:2});
}

const formatoPorcentaje = (valor) => {
    if(isNaN(valor)){
        valor = 0;
    }
    return valor.toLocaleString("en-US", {style:"percent", minimumFractionDigits:2});
}

const cargarIngresos = () => {
    let ingresosHTML = "";
    for (let i of ingresos) {
        ingresosHTML += crearIngresoHTML(i);
    }
    document.getElementById("lista-ingresos").innerHTML = ingresosHTML;
}

const crearIngresoHTML = (ingreso) => {
    let ingresoHTML = `
        <div class="elemento limpiarEstilos">
            <div class="elemento_descripcion">${ingreso.descripcion}</div>
            <div class="derecha limpiarEstilos">
                <div class="elemento_valor">+ ${formatoMoneda(ingreso.valor)}</div>
                <div class="elemento_eliminar">
                    <button class="elemento_eliminar--btn" >
                        <ion-icon name="close-circle-outline" onclick="eliminarIngreso(${ingreso.idIngreso})"></ion-icon>
                    </button>
                </div>
            </div>
        </div>
    `;
    return ingresoHTML;
}

const cargarEgresos = () => {
    let egresosHTML = "";
    for (let i of egresos) {
        egresosHTML += crearEgresoHTML(i);
    }
    document.getElementById("lista-egresos").innerHTML = egresosHTML;
}

const crearEgresoHTML = (egreso) => {
    let egresoHTML = `
        <div class="elemento limpiarEstilos">
            <div class="elemento_descripcion">${egreso.descripcion}</div>
                <div class="derecha limpiarEstilos">
                <div class="elemento_valor">- ${formatoMoneda(egreso.valor)}</div>
                <div class="elemento_porcentaje">${formatoPorcentaje(egreso.valor/totalEgresos())}</div>
                <div class="elemento_eliminar">
                    <button class="elemento_eliminar--btn">
                        <ion-icon name="close-circle-outline" onclick="eliminarEgreso(${egreso.idEgreso})"></ion-icon>
                    </button>
                </div>
            </div>
        </div>
    `;
    return egresoHTML;
}

let eliminarIngreso = (id) => {
    //Recorremos el arreglo, de ingresos y findIndex me retorna el indice
    //Comprobando que si es igual el id con el idIngreso
    let indice = ingresos.findIndex( ingreso => ingreso.idIngreso === id );
    //Se va a elminar solo un elemento
    ingresos.splice(indice, 1);
    cargarCabecero();
    cargarIngresos();
}

let eliminarEgreso = (id) => {
    let indice = egresos.findIndex( egreso => egreso.idEgreso === id );
    //Se va a elminar un elemento
    egresos.splice(indice, 1);
    cargarCabecero();
    cargarEgresos();
}

let agregarDato = () => {
    let formulario = document.forms["formulario"];
    let tipo = formulario["tipo"].value;
    let descripcion = formulario["descripcion"].value;
    let valor = formulario["valor"].value;
    if (descripcion != "" && valor != "" && +valor > 0) {
        if (tipo === "ingreso") {
            //El + sirve para pasar un string a int
            ingresos.push(new Ingreso(descripcion, +valor));
        }
        else{
            egresos.push(new Egreso(descripcion, Number(valor)));
        }
    }
    cargarApp();
}
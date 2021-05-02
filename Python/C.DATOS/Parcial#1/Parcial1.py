from flask import Flask, render_template, request
import pandas as pd
from sodapy import Socrata
import dateutil

app = Flask(__name__)
client = Socrata("www.datos.gov.co", None)
resultado = client.get("sdvb-4x4j", limit=2000)
data = pd.DataFrame.from_records(resultado)
#Conversión a date
data['fecha_resolucion'] = data['fecha_resolucion'].apply(dateutil.parser.parse)
data['fecha_corte'] = data['fecha_corte'].apply(dateutil.parser.parse)
#Cambiar el nombre de columna
data = data.rename(columns={"a_o":"año"})
#Pasar a numero la columnas
data = data.astype({"cantidad": int, "cod_territorio": int, "año": int })

data = data.fillna(value=0)

@app.route('/')
def principal():
    return render_template('index.html',  data=[data.to_html()])

@app.route('/consultar', methods=("POST", "GET"))
def consultar():
    info = pd.DataFrame
    if request.method == "POST":
        respuesta = request.form["question"]
        print(respuesta)
        if respuesta == "c1":
            info = (data.groupby('laboratorio_vacuna')['cantidad'].sum()).to_frame().to_html()
        if respuesta == "c2":
            info = (data.groupby('nom_territorio')['cantidad'].max()).to_frame().to_html()
        if respuesta == "c3":
            info = (data.groupby('nom_territorio')['cantidad'].sum()).to_frame().to_html()
        if respuesta == "c4":
            info = (data.groupby(data['nom_territorio'])['cantidad'].mean()).to_frame().to_html()
        if respuesta == "c5":
            info = (data.groupby(data['laboratorio_vacuna'])['cantidad'].mean()).to_frame().to_html()
        if respuesta == "c6":
            info = (data.groupby('laboratorio_vacuna')['cantidad'].max()).to_frame().to_html()
        if respuesta == "c7":
            info = (data[data['cantidad']==data['cantidad'].max()]).to_html()
        if respuesta == "c8":
            info = (data.groupby('uso_vacuna')['cantidad'].sum()).to_frame().to_html()
        if respuesta == "c9":
            tot=data['cantidad'].sum()
            d={'Total':['Total'],'Valor':[tot]}
            info = (pd.DataFrame(d)).to_html()
        if respuesta == "c10":
            info = (data.groupby(['nom_territorio', 'laboratorio_vacuna'])['cantidad'].count()).to_frame().to_html()
        if respuesta == "c11":
            info = (data.groupby('fecha_resolucion')['cantidad'].sum()).to_frame().to_html()
        if respuesta == "c1_1":
            select = request.form.get('select')
            info = (data[data['laboratorio_vacuna']==select]).to_html()
        if respuesta == "c2_2":
            select = request.form.get('territorium')
            info = (data[data['nom_territorio']==select]).to_html()
        if respuesta == "c12":
            lista = request.form.getlist('columna')
            print(lista)
            info = data[lista].to_html()
        if respuesta == "c11_11":
            fecha = request.form.get('fecha')
            info = (data[data['fecha_resolucion']==fecha]).to_html()
        if respuesta == "c8_8":
            area = request.form.get('textarea')
            info = (data[data['uso_vacuna']==area]).to_html()
    return render_template('consultas.html', data=[info])

if __name__ == '__main__':
    app.run(debug=True)
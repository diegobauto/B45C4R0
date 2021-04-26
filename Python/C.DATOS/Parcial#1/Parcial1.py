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
    return render_template('index.html',  tables=[data.to_html()])

@app.route('/consultar', methods=("POST", "GET"))
def consultar():
    info = pd.DataFrame
    if request.method == "POST":
        if request.form["question"] == "c1":
            info = (data.groupby('laboratorio_vacuna')['cantidad'].sum()).to_frame().to_html()
        if request.form["question"] == "c2":
            info = (data.groupby('nom_territorio')['cantidad'].max()).to_frame().to_html()
        if request.form["question"] == "c3":
            info = (data.groupby('nom_territorio')['cantidad'].sum()).to_frame().to_html()
        if request.form["question"] == "c4":
            info = (data.groupby(data['nom_territorio'])['cantidad'].mean()).to_frame().to_html()
        if request.form["question"] == "c5":
            info = (data.groupby(data['laboratorio_vacuna'])['cantidad'].mean()).to_frame().to_html()
        if request.form["question"] == "c6":
            info = (data.groupby('laboratorio_vacuna')['cantidad'].max()).to_frame().to_html()
        if request.form["question"] == "c7":
            info = (data[data['cantidad']==data['cantidad'].max()]).to_html()
        if request.form["question"] == "c8":
            info = (data.groupby('uso_vacuna')['cantidad'].sum()).to_frame().to_html()
        if request.form["question"] == "c9":
            tot=data['cantidad'].sum()
            d={'Total':['Total'],'Valor':[tot]}
            info = (pd.DataFrame(d)).to_html()
        if request.form["question"] == "c10":
            info = (data.groupby(['nom_territorio', 'laboratorio_vacuna'])['cantidad'].count()).to_frame().to_html()
        if request.form["question"] == "c11":
            info = (data.groupby('fecha_resolucion')['cantidad'].sum()).to_frame().to_html()
    return render_template('consultas.html', tables=[info])

if __name__ == '__main__':
    app.run(debug=True)
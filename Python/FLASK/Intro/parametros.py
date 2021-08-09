from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f"Saludos {nombre.upper()}"

@app.route("/sumar/<int:numero1>/<int:numero2>")
def sumar(numero1,numero2):
    return f"Suma: {numero1+numero2}"

if __name__ == "__main__":
    app.run(debug=True)
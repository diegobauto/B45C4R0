from flask import Flask, session
from flask import render_template, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "Mi_llave_secreta" #Una llave para el concepto de sesiones

@app.route("/")
def home():
    if "username" in session:
        return f"El usuario ya ha hecho login {session['username']}"
    return "No ha hecho login"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        # Omitimos validacion de usuario y password
        usuario = request.form["username"] #Obtenemos el valor del formulario
        # Agregar el usuario a la sesion
        session["username"] = usuario
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
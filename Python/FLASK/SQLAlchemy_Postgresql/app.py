from flask import Flask, render_template, url_for, redirect, request
from flask_migrate import Migrate
from credenciales import *
from database import db
from forms import PersonaForm
from models import Persona

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
#No haga un rastreo de cada una de las modificaciones que estamos realizando sobre la base de datos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Inicializacion del objeto db de sqlalchemy
#db = SQLAlchemy(app)
db.init_app(app)

#Configuracion de flask migrate para hacer las migraciones y se cree el mapeo
# de esta clase de python hacia la base de datos
migrate = Migrate()
migrate.init_app(app, db) #Le pasamos la variable app y el db de alchemy

app.config["SECRET_KEY"] = "llave_secreta" #Configuracion de flask-wtf

@app.route("/")
def inicio():
    #Listado personas
    personas = Persona.query.all() #Trae todas las personas de la base de datos
    total_personas = Persona.query.count() #Cuenta cuantas personas hay en la base de datos
    return render_template("index.html", personas=personas, total=total_personas)


@app.route("/ver_persona/<int:id>")
def verPersona(id):
    #Recuperar persona por el id
    #persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)#Comprobar si no encuentra id, manda a la pagina de error
    return render_template("ver_persona.html", persona=persona)


@app.route("/agregar_persona", methods=["GET", "POST"])
def agregarPersona():
    persona = Persona() #Creamos un objeto de tipo Persona
    personaForm = PersonaForm(obj=persona) #Le asociamos la clase de modelo al formulario html
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona) #Se llena el objeto persona con los valores del formulario
            db.session.add(persona) #Insertamos el registro a la base de datos
            db.session.commit() #Guardamos los cambios de la insersión
            return redirect(url_for("inicio"))
    return render_template("agregar.html", form=personaForm)

if __name__ == "__main__":
    app.run(debug=True)
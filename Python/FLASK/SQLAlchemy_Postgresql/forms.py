from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#Se crea una clase de tipo FlaskForm para obtener un formulario de tipo html
#Para eso se hizo la instalación de flask-wtf
class PersonaForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    apellido = StringField("Apellido: ",) #No es requerido
    email = StringField("Email: ", validators=[DataRequired()])
    enviar = SubmitField("Enviar")
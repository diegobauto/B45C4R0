#Configuración de la base de datos
USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "sap_flask_db"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"
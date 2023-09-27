# routes.py
from flask import Blueprint

# Crea un Blueprint
Data_Controller = Blueprint('data', __name__, url_prefix='/data')


# Define la ruta de inicio
@Data_Controller.route('/')
def home():
    return "¡Hola, mundo!"

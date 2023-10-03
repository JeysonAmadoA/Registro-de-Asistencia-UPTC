from flask import Blueprint, send_file
from Services.Implementation.Data_file_Service import Data_file_Service
import os

# Crea un Blueprint
File_Controller = Blueprint('file', __name__, url_prefix='/file')


@File_Controller.route('/generar_archivo_sistemas')
def index_systems_engineer():
    data_file = Data_file_Service()
    zip_filename = data_file.generate_systems_engineer_file()
    if os.path.isfile(zip_filename):
        return send_file(zip_filename, as_attachment=True)
    else:
        msg = "El archivo Zip no existe."
        return msg


@File_Controller.route('/generar_archivo_electronica')
def index_electronic_engineer():
    pass


@File_Controller.route('/generar_archivo_profesores')
def index_teachers():
    pass


@File_Controller.route('/generar_archivo_otros')
def index_others():
    pass

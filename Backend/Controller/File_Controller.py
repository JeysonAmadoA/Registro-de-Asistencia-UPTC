from flask import Blueprint, send_file
from Services.Implementation.Data_file_Service import Data_file_Service
import os

File_Controller = Blueprint('file', __name__, url_prefix='/file')


@File_Controller.route('/generar_archivo_sistemas')
def download_systems_engineer_files():
    data_file_service = Data_file_Service()
    zip_filename = data_file_service.generate_systems_engineer_file()
    return __validate_zip_file(zip_filename)

@File_Controller.route('/generar_archivo_electronica')
def download_electronic_engineer_files():
    data_file_service = Data_file_Service()
    zip_filename = data_file_service.generate_electronic_engineer_file()
    return __validate_zip_file(zip_filename)


@File_Controller.route('/generar_archivo_profesores')
def download_teachers_files():
    data_file_service = Data_file_Service()
    zip_filename = data_file_service.generate_teachers_file()
    return __validate_zip_file(zip_filename)

@File_Controller.route('/generar_archivo_otros')
def download_others_files():
    data_file_service = Data_file_Service()
    zip_filename = data_file_service.generate_others_file()
    return __validate_zip_file(zip_filename)

def __validate_zip_file(zip_filename):
    if os.path.isfile(zip_filename):
        return send_file(zip_filename, as_attachment=True)
    else:
        return "El archivo Zip no existe."

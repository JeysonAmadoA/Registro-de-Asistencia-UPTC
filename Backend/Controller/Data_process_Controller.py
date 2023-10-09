from flask import Blueprint, jsonify
from Services.Implementation.Data_process_Service import Data_process_Service
from Services.Implementation.Index_data_Service import Index_data_Service
import os

Data_process_Controller = Blueprint('data_process', __name__, url_prefix='/process')


@Data_process_Controller.route('/register_data_default')
def register_data_default():
    register_file_path = os.path.abspath('Storage/Registro/Registro_Evento.csv')
    register_data_process = Data_process_Service()
    register_data_process.set_dataframe(register_file_path)
    register_data_process.clean_register_data()
    register_data_process.process_register_data()
    register_data_process.store_register_data()

    response_data = {
        "message": "Información de registro almacenada"
    }

    return jsonify(response_data), 200



@Data_process_Controller.route('/register_assistance')
def register_assistance():

    directorio = 'Storage/Asistencia'
    event_model = Index_data_Service('Events').get_model()
    archivos = os.listdir(directorio)

    for archivo in archivos:
        if os.path.isfile(os.path.join(directorio, archivo)):
            file_path = os.path.join(directorio, archivo)
            archive_date = archivo[:10]
            event_register = event_model.filter_by_event_date(archive_date)
            if event_register is None:
                register_data_process = Data_process_Service()
                register_data_process.set_dataframe(file_path)
                register_data_process.clean_data(archive_date)
                register_data_process.process_data()
                register_data_process.store_process_data()

    response_data = {
        "message": "Información de asistencia almacenada"
    }

    return jsonify(response_data), 200

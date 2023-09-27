from flask import Blueprint
from Services.Implementation.Data_process_Service import Data_process_Service
import os

Data_process_Controller = Blueprint('data_process', __name__, url_prefix='/process')


@Data_process_Controller.route('/register_data_default')
def register_data_default():
    register_file_path = os.path.abspath('Storage/Registro_Evento.csv')
    register_data_process = Data_process_Service()
    register_data_process.set_dataframe(register_file_path)
    register_data_process.clean_register_data()
    register_data_process.process_register_data()
    register_data_process.store_register_data()


    return "Información de registro almacenada"

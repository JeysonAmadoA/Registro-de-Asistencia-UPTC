from Config.Server import app
from Services.Implementation.Data_process_Service import Data_process_Service
import os

if __name__ == '__main__':
    print('Iniciando Servidor')
    app.run(host='0.0.0.0', port=5000, debug=True)
    # register_file_path = os.path.abspath('Storage/Registro/Registro_Evento.csv')
    # register_data_process = Data_process_Service()
    # register_data_process.set_dataframe(register_file_path)
    # register_data_process.clean_register_data()
    # register_data_process.process_register_data()
    # register_data_process.store_register_data()


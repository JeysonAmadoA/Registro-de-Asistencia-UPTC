from Config.Server import app
from Services.Implementation.Data_file_Service import Data_file_Service
import os

if __name__ == '__main__':
    print('Iniciando Servidor')
    app.run(host='0.0.0.0', port=5000, debug=True)
    # data_file = Data_file_Service()
    # data_file.generate_systems_engineer_file()

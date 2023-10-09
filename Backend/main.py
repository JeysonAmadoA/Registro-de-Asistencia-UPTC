from Config.Server import app
from Services.Implementation.Data_process_Service import Data_process_Service

if __name__ == '__main__':
    print('Iniciando Servidor')
    app.run(host='0.0.0.0', port=5000, debug=True)
    


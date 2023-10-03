from flask import Flask
from flask_cors import CORS
from Controller.Data_Controller import Data_Controller
from Controller.Data_process_Controller import Data_process_Controller
from Controller.File_Controller import File_Controller

app = Flask(__name__)

CORS(app)

app.register_blueprint(Data_Controller)
app.register_blueprint(Data_process_Controller)
app.register_blueprint(File_Controller)


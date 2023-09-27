from flask import Flask
from Controller.Data_Controller import Data_Controller
from Controller.Data_process_Controller import Data_process_Controller

app = Flask(__name__)

app.register_blueprint(Data_Controller)
app.register_blueprint(Data_process_Controller)


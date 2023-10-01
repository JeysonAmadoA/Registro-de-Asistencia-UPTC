from flask import Blueprint, jsonify
from Services.Implementation.Index_data_Service import Index_data_Service

# Crea un Blueprint
Data_Controller = Blueprint('data', __name__, url_prefix='/data')


# Define la ruta de inicio
@Data_Controller.route('/ingenieria_de_sistemas')
def index_systems_engineer():
    systems_engineer = Index_data_Service()
    return jsonify(systems_engineer.index_systems_engineer())


@Data_Controller.route('/ingenieria_electronica')
def index_electronic_engineer():
    electronic_engineer = Index_data_Service()
    return jsonify(electronic_engineer.index_electronic_engineer())


@Data_Controller.route('/docentes')
def index_teachers():
    teachers = Index_data_Service()
    return jsonify(teachers.index_teachers())


@Data_Controller.route('/otros')
def index_others():
    other = Index_data_Service()
    return jsonify(other.index_other())

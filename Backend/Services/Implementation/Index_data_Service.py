from Services.Interfaces.Index_data_interface import Index_data_interface
from Config import Global_Helpers


class Index_data_Service(Index_data_interface):
    def __init__(self, table_name):
        self.table_name = table_name

    def get_all(self):
        model = self.get_model()
        if model:
            try:
                return model.get_all()
            except Exception as e:
                print("Ocurrió un error al obtener registros:", e)
        else:
            raise ValueError("Model not found for table name")

    def filter_by_id(self, id):
        model = self.get_model()
        if model:
            try:
                return model.get_by_id(id)
            except Exception as e:
                print("Ocurrió un error al obtener registro:", e)
        else:
            raise ValueError("Model not found for table name")

    def get_model(self):
        return Global_Helpers.get_model(self.table_name)

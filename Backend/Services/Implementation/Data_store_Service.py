from Services.Interfaces.Data_store_Interface import Data_store_Interface
from Config import Global_Helpers


class Data_store_Service(Data_store_Interface):
    def __init__(self, table_name):
        self.table_name = table_name

    def create_instance(self, data):
        model = Global_Helpers.get_model(self.table_name)
        if model:
            try:
                instance = model(**data)
                instance.store()
                return instance
            except Exception as e:
                print("Ocurrió un error al crear registro:", e)
        else:
            raise ValueError("Model not found for table name")

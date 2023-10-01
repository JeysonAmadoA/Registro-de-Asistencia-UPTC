from Services.Interfaces.Data_store_Interface import Data_store_Interface
from Config import Global_Helpers


class Data_store_Service(Data_store_Interface):

    instances = []

    def __init__(self, table_name):
        self.table_name = table_name
        self.model = Global_Helpers.get_model(self.table_name)

    def begin_transaction(self):
        self.model.begin()

    def add_instance(self, data):
        if self.model:
            try:
                instance = self.model(**data)
                self.instances.append(instance)
            except Exception as e:
                print("Ocurrió un error al agregar registro:", e)
        else:
            raise ValueError("Model not found for table name")

    def end_transaction(self):
        model = self.model()
        model.commit()

    def massive_store(self):
        model = self.model()
        model.bulk_insert(self.instances)
        self.instances = []





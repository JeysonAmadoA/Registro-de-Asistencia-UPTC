from abc import ABC, abstractmethod


class Data_process_Interface(ABC):

    @abstractmethod
    def set_dataframe(self, file_path):
        pass

    @abstractmethod
    def clean_data(self, event_date):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def store_process_data(self):
        pass

    @abstractmethod
    def clean_register_data(self):
        pass

    @abstractmethod
    def process_register_data(self):
        pass

    @abstractmethod
    def store_register_data(self):
        pass

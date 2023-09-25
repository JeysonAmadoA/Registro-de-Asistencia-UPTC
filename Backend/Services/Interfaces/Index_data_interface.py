from abc import ABC, abstractmethod


class Index_data_interface(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def filter_by_id(self, id):
        pass

    @abstractmethod
    def get_model(self):
        pass

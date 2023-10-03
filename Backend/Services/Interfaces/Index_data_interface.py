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

    @abstractmethod
    def index_systems_engineer(self):
        pass

    @abstractmethod
    def index_electronic_engineer(self):
        pass

    @abstractmethod
    def index_teachers(self):
        pass

    @abstractmethod
    def index_other(self):
        pass

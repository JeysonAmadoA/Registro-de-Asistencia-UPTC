from abc import ABC, abstractmethod


class Data_store_Interface(ABC):

    @abstractmethod
    def create_instance(self, data):
        pass


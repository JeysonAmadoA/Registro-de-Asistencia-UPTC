from abc import ABC, abstractmethod


class Data_store_Interface(ABC):

    @abstractmethod
    def begin_transaction(self):
        pass

    @abstractmethod
    def add_instance(self, data):
        pass

    @abstractmethod
    def massive_store(self):
        pass

    @abstractmethod
    def end_transaction(self):
        pass

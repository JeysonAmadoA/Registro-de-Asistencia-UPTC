from abc import ABC, abstractmethod


class Data_file_Interface(ABC):

    @abstractmethod
    def generate_systems_engineer_file(self):
        pass

    @abstractmethod
    def generate_electronic_engineer_file(self):
        pass

    @abstractmethod
    def generate_teachers_file(self):
        pass

    @abstractmethod
    def generate_others_file(self):
        pass

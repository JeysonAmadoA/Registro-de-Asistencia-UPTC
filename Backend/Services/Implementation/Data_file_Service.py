from Services.Interfaces.Data_file_Interface import Data_file_Interface
from Services.Implementation.Index_data_Service import Index_data_Service
import pandas as panda
import matplotlib.pyplot as plot
import os
import zipfile


class Data_file_Service(Data_file_Interface):
    index_service = Index_data_Service()

    def generate_systems_engineer_file(self):
        data = self.index_service.index_systems_engineer()
        return self.__generate_files(data, 'Sistemas')
        

    def generate_electronic_engineer_file(self):
        data = self.index_service.index_electronic_engineer()
        return self.__generate_files(data, 'Electrónica')

    def generate_teachers_file(self):
        data = self.index_service.index_teachers()
        return self.__generate_files(data, 'Docentes')

    def generate_others_file(self):
        data = self.index_service.index_other()
        return self.__generate_files(data, 'Por revisar')
    
    def __generate_files(self, data, filename):
        dataframe = panda.DataFrame(data)
        asignatura_counts = dataframe['Asignatura'].value_counts()
        plot.figure(figsize=(8, 8))
        asignatura_counts.plot.pie(autopct='%1.1f%%')
        plot.title('Porcentaje de Datos por Asignatura')
        plot.ylabel('')

        graficos_directory = 'Storage/Graficos'
        os.makedirs(graficos_directory, exist_ok=True)
        graficos_filename = os.path.join(graficos_directory, filename + '.png')
        plot.savefig(graficos_filename)

        excel_directory = 'Storage/Xlsx'
        os.makedirs(excel_directory, exist_ok=True)
        excel_filename = os.path.join(excel_directory, filename + '.xlsx')
        dataframe.to_excel(excel_filename, index=False)

        with zipfile.ZipFile('Storage/Zips/'+ filename +'.zip', 'w') as archivo_zip:
            archivo_zip.write(graficos_filename, arcname = filename + '.png')
            archivo_zip.write(excel_filename, arcname = filename + '.xlsx')

        path_zip_file = 'Storage/Zips/'+ filename +'.zip'
        absolute_path_zip_file = os.path.abspath(path_zip_file)

        return absolute_path_zip_file

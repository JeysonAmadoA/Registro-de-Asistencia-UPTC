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
        dataframe = panda.DataFrame(data)
        asignatura_counts = dataframe['Asignatura'].value_counts()
        plot.figure(figsize=(8, 8))
        asignatura_counts.plot.pie(autopct='%1.1f%%')
        plot.title('Porcentaje de Datos por Asignatura')
        plot.ylabel('')

        # Crear directorios y archivos
        graficos_directory = 'Storage/Graficos'
        os.makedirs(graficos_directory, exist_ok=True)
        graficos_filename = os.path.join(graficos_directory, 'Sistemas.png')
        plot.savefig(graficos_filename)

        excel_directory = 'Storage/Xlsx'
        os.makedirs(excel_directory, exist_ok=True)
        excel_filename = os.path.join(excel_directory, 'data.xlsx')
        dataframe.to_excel(excel_filename, index=False)

        with zipfile.ZipFile('Storage/Zips/Sistemas.zip', 'w') as archivo_zip:
            archivo_zip.write(graficos_filename, arcname='Sistemas.png')
            archivo_zip.write(excel_filename, arcname='data.xlsx')

        ruta_archivo_zip = 'Storage/Zips/Sistemas.zip'
        ruta_absoluta = os.path.abspath(ruta_archivo_zip)

        return ruta_absoluta

    def generate_electronic_engineer_file(self):
        pass

    def generate_teachers_file(self):
        pass

    def generate_others_file(self):
        pass

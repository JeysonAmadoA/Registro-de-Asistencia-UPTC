from Services.Interfaces.Data_process_Interface import Data_process_Interface
import pandas as panda


class Data_process_Service(Data_process_Interface):

    dataframe = None
    subjects = None
    program = None
    assistants = None

    def set_dataframe(self, file_path):
        Data_process_Service.dataframe = panda.read_csv(file_path)

    def clean_data(self, file_path):
        # Implementa la lógica para cargar datos desde el archivo
        pass

    def process_data(self, data):
        # Implementa la lógica para procesar los datos
        pass

    def store_process_data(self, data, output_file):
        # Implementa la lógica para guardar los datos en un archivo de salida
        pass

    def clean_register_data(self):
        dataframe = Data_process_Service.dataframe
        dataframe['Programa Académico'] = dataframe['Programa Académico'].fillna('No registra')

        dataframe['Nombre'] = dataframe['Nombre'].str.strip()
        dataframe['Correo institucional'] = dataframe['Correo institucional'].str.strip()
        dataframe['Programa Académico'] = dataframe['Programa Académico'].str.strip()
        dataframe['Asignatura'] = dataframe['Asignatura'].str.strip()

        dataframe['Asignatura'].fillna('No Registra', inplace=True)
        dataframe['Nombre'].fillna('No Registra', inplace=True)
        dataframe['Nombre'] = dataframe['Nombre'].str.title()

        mask = dataframe['Asignatura'].str.contains('trans', case=False, regex=True)
        dataframe.loc[mask, 'Asignatura'] = 'Transmisión de datos'

        mask = dataframe['Asignatura'].str.contains('trans', case=False, regex=True)
        dataframe.loc[mask, 'Asignatura'] = 'Transmisión de datos'
        dataframe = Data_process_Service.__clean_electronic_ing_data(self, dataframe)
        dataframe = Data_process_Service.__clean_systems_ing_data(self, dataframe)

        Data_process_Service.dataframe = dataframe
        # Obtener los valores únicos de la columna 'Asignatura' del DataFrame 'resultado'
        resultado = Data_process_Service.dataframe.query("`Programa Académico` == 'Ingeniería de Sistemas y Computación'")
        # resultado = dataframe.query("`Programa Académico` == 'Ingeniería Electrónica'")
        print(resultado['Asignatura'].unique())

    def __clean_electronic_ing_data(self, dataframe):
        electronic_ing_filter = dataframe['Programa Académico'] == 'Ingeniería Electrónica'
        communication_filter = dataframe.loc[electronic_ing_filter, 'Asignatura'].str.contains('comu', case=False, regex=True)
        dataframe.loc[electronic_ing_filter & communication_filter, 'Asignatura'] = 'Comunicaciones II'

        telematic_filter = dataframe.loc[electronic_ing_filter, 'Asignatura'].str.contains('tele', case=False, regex=True)
        dataframe.loc[electronic_ing_filter & telematic_filter, 'Asignatura'] = 'Telemática'

        return dataframe

    def __clean_systems_ing_data(self, dataframe):
        systems_ing_filter = dataframe['Programa Académico'] == 'Ingeniería de Sistemas y Computación'

        io_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('investi', case=False, regex=True)
        dataframe.loc[systems_ing_filter & io_filter, 'Asignatura'] = 'Investigación de Operaciones'

        communication_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('comu', case=False, regex=True)
        dataframe.loc[systems_ing_filter & communication_filter, 'Asignatura'] = 'Comunicaciones'

        elective_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('electiva iii', case=False, regex=True)
        dataframe.loc[systems_ing_filter & elective_filter, 'Asignatura'] = 'Electiva III: Gestion de redes'

        network_mng_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('gesti', case=False, regex=True)
        dataframe.loc[systems_ing_filter & network_mng_filter, 'Asignatura'] = 'Electiva III: Gestion de redes'

        research_group_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('semillero', case=False, regex=True)
        dataframe.loc[systems_ing_filter & research_group_filter, 'Asignatura'] = 'Electiva III: Gestion de redes'

        return dataframe

    def process_register_data(self):
        Data_process_Service.subjects = Data_process_Service.dataframe['Asignatura'].unique()
        Data_process_Service.program = Data_process_Service.dataframe['Programa Académico'].unique()
        Data_process_Service.assistants = Data_process_Service.dataframe

        print(Data_process_Service.assistants)


    def store_register_data(self, data, output_file):

        pass


data_service = Data_process_Service()
data_service.set_dataframe("../../Storage/Registro_Evento.csv")
data_service.clean_register_data()
data_service.process_register_data()

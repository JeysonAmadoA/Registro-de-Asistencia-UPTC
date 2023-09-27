from Services.Interfaces.Data_process_Interface import Data_process_Interface
from Services.Implementation.Index_data_Service import Index_data_Service
from Services.Implementation.Data_store_Service import Data_store_Service
import pandas as panda


class Data_process_Service(Data_process_Interface):
    dataframe = None
    subjects = None
    programs = None
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
        dataframe['Correo institucional'] = dataframe['Correo institucional'].str.strip().str.lower()
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

    def __clean_electronic_ing_data(self, dataframe):
        electronic_ing_filter = dataframe['Programa Académico'] == 'Ingeniería Electrónica'
        communication_filter = dataframe.loc[electronic_ing_filter, 'Asignatura'].str.contains('comu', case=False,
                                                                                               regex=True)
        dataframe.loc[electronic_ing_filter & communication_filter, 'Asignatura'] = 'Comunicaciones II'

        telematic_filter = dataframe.loc[electronic_ing_filter, 'Asignatura'].str.contains('tele', case=False,
                                                                                           regex=True)
        dataframe.loc[electronic_ing_filter & telematic_filter, 'Asignatura'] = 'Telemática'

        return dataframe

    def __clean_systems_ing_data(self, dataframe):
        systems_ing_filter = dataframe['Programa Académico'] == 'Ingeniería de Sistemas y Computación'

        io_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('investi', case=False, regex=True)
        dataframe.loc[systems_ing_filter & io_filter, 'Asignatura'] = 'Investigación de Operaciones'

        communication_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('comu', case=False,
                                                                                            regex=True)
        dataframe.loc[systems_ing_filter & communication_filter, 'Asignatura'] = 'Comunicaciones'

        elective_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('electiva iii', case=False,
                                                                                       regex=True)
        dataframe.loc[systems_ing_filter & elective_filter, 'Asignatura'] = 'Electiva III: Gestion de redes'

        network_mng_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('gesti', case=False,
                                                                                          regex=True)
        dataframe.loc[systems_ing_filter & network_mng_filter, 'Asignatura'] = 'Electiva III: Gestion de redes'

        research_group_filter = dataframe.loc[systems_ing_filter, 'Asignatura'].str.contains('semillero', case=False,
                                                                                             regex=True)
        dataframe.loc[systems_ing_filter & research_group_filter, 'Asignatura'] = 'Electiva III: Gestion de redes'

        return dataframe

    def process_register_data(self):
        Data_process_Service.subjects = Data_process_Service.dataframe['Asignatura'].unique()
        Data_process_Service.subjects = [{"subject_name": item} for item in Data_process_Service.subjects if item]

        Data_process_Service.programs = Data_process_Service.dataframe['Programa Académico'].unique()
        Data_process_Service.programs = [{"program_name": item} for item in Data_process_Service.programs if item]

        Data_process_Service.assistants = Data_process_Service.dataframe.to_dict(orient='records')

    def store_register_data(self):
        self.__store_subjects()
        self.__store_programs()
        self.__store_assistants()
        self.__reset_data()

    def __store_subjects(self):
        store_subject_service = Data_store_Service('Subjects')
        subject_model = Index_data_Service('Subjects').get_model()

        for subject in Data_process_Service.subjects:
            subject_exist = subject_model.filter_by_subject_name(subject['subject_name'])
            if subject_exist:
                print("Ya está registrada la asignatura")
            else:
                store_subject_service.add_instance(subject)

        store_subject_service.massive_store()

    def __store_programs(self):
        store_program_service = Data_store_Service('Programs')
        program_model = Index_data_Service('Programs').get_model()
        print(Data_process_Service.programs)
        for program in Data_process_Service.programs:
            program_exist = program_model.filter_by_program_name(program['program_name'])
            if program_exist:
                print("Ya está registrado el programa")
            else:
                store_program_service.add_instance(program)

        store_program_service.massive_store()

    def __store_assistants(self):
        self.__adjust_assistant_data()

        store_assistant_service = Data_store_Service('Assistants')
        assistant_model = Index_data_Service('Assistants').get_model()
        for assistant in Data_process_Service.assistants:
            assistant_exist = assistant_model.filter_by_email(assistant['email'])
            if assistant_exist:
                print("Ya está registrado el asistente")
            else:
                store_assistant_service.add_instance(assistant)

        store_assistant_service.massive_store()

    def __adjust_assistant_data(self):
        index_programs = Index_data_Service('Programs').get_model()
        index_subjects = Index_data_Service('Subjects').get_model()

        Data_process_Service.assistants = [
            {
                "name": item["Nombre"],
                "email": item["Correo institucional"],
                "program_id": index_programs.filter_by_program_name(
                    item['Programa Académico']).id if index_programs.filter_by_program_name(
                    item['Programa Académico']) is not None else None,
                "subject_id": index_subjects.filter_by_subject_name(
                    item['Asignatura']).id if index_subjects.filter_by_subject_name(
                    item['Asignatura']) is not None else None,
            }
            for item in Data_process_Service.assistants
        ]

    def __reset_data(self):
        Data_process_Service.dataframe = None
        Data_process_Service.subjects = None
        Data_process_Service.programs = None
        Data_process_Service.assistants = None

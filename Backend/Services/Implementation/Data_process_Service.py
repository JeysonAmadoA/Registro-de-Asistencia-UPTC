from Services.Interfaces.Data_process_Interface import Data_process_Interface
from Services.Implementation.Index_data_Service import Index_data_Service
from Services.Implementation.Data_store_Service import Data_store_Service
import pandas as panda


class Data_process_Service(Data_process_Interface):
    dataframe = None
    event = None
    subjects = []
    programs = []
    assistants = []
    assistance = []

    def set_dataframe(self, file_path):
        Data_process_Service.dataframe = panda.read_csv(file_path)

    def clean_data(self, event_date):
        dataframe = Data_process_Service.dataframe
        dataframe['Nombre'] = dataframe['Nombre'].str.strip().str.title()
        dataframe['Apellido'] = dataframe['Apellido'].str.strip().str.title()
        dataframe['Correo electrónico'] = dataframe['Correo electrónico'].str.strip().str.lower()
        dataframe['Duración'] = dataframe['Duración'].str.strip()
        dataframe['Hora a la que se unió'] = dataframe['Hora a la que se unió'].str.strip()
        dataframe['Hora a la que salió'] = dataframe['Hora a la que salió'].str.strip()
        dataframe.fillna('No Registra', inplace=True)

        dataframe['Hora a la que se unió'] = event_date + ' ' + dataframe['Hora a la que se unió']
        dataframe['Hora a la que salió'] = event_date + ' ' + dataframe['Hora a la que salió']

        Data_process_Service.dataframe = dataframe
        Data_process_Service.event = {"event_date": event_date}

    def process_data(self):
        Data_store_Service('Programs')
        Data_store_Service('Subjects')
        index_data_assistant = Index_data_Service('Assistants').get_model()
        for index, row in Data_process_Service.dataframe.iterrows():
            name = row['Nombre']
            last_name = row['Apellido']
            email = row['Correo electrónico']
            assistant_registered = index_data_assistant.filter_by_email(email)

            if assistant_registered is None:
                Data_process_Service.assistants.append({"name": name + ' ' + last_name,
                                                        "email": email,
                                                        "subject_id": None,
                                                        "program_id": None})

        self.__store_event()
        self.__store_assistants()

    def store_process_data(self):
        index_event = Index_data_Service('Events').get_model()
        index_assistant = Index_data_Service('Assistants').get_model()
        store_assistance_service = Data_store_Service('Assistance_records')

        for index, row in Data_process_Service.dataframe.iterrows():
            email = row['Correo electrónico']
            duration = row['Duración']
            entry_hour = row['Hora a la que se unió']
            departure_hour = row['Hora a la que salió']

            self.assistance.append({"event_id": index_event.filter_by_event_date(self.event['event_date']).id,
                                    "assistant_id": index_assistant.filter_by_email(email).id,
                                    "duration_time": duration,
                                    "entry_hour": entry_hour,
                                    "departure_hour": departure_hour})

        for assistance in self.assistance:
            store_assistance_service.add_instance(assistance)

        store_assistance_service.massive_store()
        self.__reset_data()

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
        self.__adjust_assistant_data()
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
        for program in Data_process_Service.programs:
            program_exist = program_model.filter_by_program_name(program['program_name'])
            if program_exist:
                print("Ya está registrado el programa")
            else:
                store_program_service.add_instance(program)

        store_program_service.massive_store()

    def __store_assistants(self):
        store_assistant_service = Data_store_Service('Assistants')
        assistant_model = Index_data_Service('Assistants').get_model()
        for assistant in Data_process_Service.assistants:
            assistant_exist = assistant_model.filter_by_email(assistant['email'])
            print(assistant_exist)
            if assistant_exist:
                print("Ya está registrado el asistente")
            else:
                store_assistant_service.add_instance(assistant)

        print(store_assistant_service.instances)
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
        Data_process_Service.subjects = []
        Data_process_Service.programs = []
        Data_process_Service.assistants = []
        Data_process_Service.assistance = []

    def __store_event(self):
        store_event_service = Data_store_Service('Events')
        event_model = Index_data_Service('Events').get_model()
        event_exist = event_model.filter_by_event_date(self.event['event_date'])
        if event_exist:
            print("Ya está registrado evento")
        else:
            store_event_service.add_instance(Data_process_Service.event)

        store_event_service.massive_store()

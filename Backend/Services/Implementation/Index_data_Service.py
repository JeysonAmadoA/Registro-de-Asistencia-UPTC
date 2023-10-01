from builtins import print

from Services.Interfaces.Index_data_interface import Index_data_interface
from Config import Global_Helpers
import os


class Index_data_Service(Index_data_interface):
    def __init__(self, table_name=None):
        self.table_name = table_name

    def get_all(self):
        model = self.get_model()
        if model:
            try:
                return model.get_all()
            except Exception as e:
                print("Ocurrió un error al obtener registros:", e)
        else:
            raise ValueError("Model not found for table name")

    def filter_by_id(self, id):
        model = self.get_model()
        if model:
            try:
                return model.get_by_id(id)
            except Exception as e:
                print("Ocurrió un error al obtener registro:", e)
        else:
            raise ValueError("Model not found for table name")

    def get_model(self):
        return Global_Helpers.get_model(self.table_name)

    def index_systems_engineer(self):
        self.table_name = 'Programs'
        program_model = self.get_model()
        self.table_name = 'Assistants'
        assistants = self.get_model().filter_by_program_id(program_model.filter_by_program_name('Ingeniería de '
                                                                                                'Sistemas y '
                                                                                                'Computación').id)
        systems_engineer = self.denormalize_assistant_data(assistants)
        return systems_engineer

    def index_electronic_engineer(self):
        self.table_name = 'Programs'
        program_model = self.get_model()
        self.table_name = 'Assistants'
        assistants = self.get_model().filter_by_program_id(
            program_model.filter_by_program_name('Ingeniería Electrónica').id)
        electronic_engineer = self.denormalize_assistant_data(assistants)
        return electronic_engineer

    def index_teachers(self):
        self.table_name = 'Programs'
        program_model = self.get_model()
        self.table_name = 'Assistants'
        assistants = self.get_model().filter_by_program_id(
            program_model.filter_by_program_name('Docente').id)
        teachers = self.denormalize_assistant_data(assistants)
        return teachers

    def index_other(self):
        self.table_name = 'Programs'
        program_model = self.get_model()
        systems_id = program_model.filter_by_program_name('Ingeniería de Sistemas y Computación').id
        electronic_id = program_model.filter_by_program_name('Ingeniería Electrónica').id
        teachers_id = program_model.filter_by_program_name('Docente').id
        programs_exclude = [systems_id, electronic_id, teachers_id]
        self.table_name = 'Assistants'
        assistants = self.get_model().filter_where_not_in_programs(programs_exclude)
        others = self.denormalize_assistant_data(assistants)
        return others

    def denormalize_assistant_data(self, assistants):
        data_result = []
        self.table_name = 'Events'
        events = self.get_all()
        self.table_name = 'Programs'
        program_model = self.get_model()
        self.table_name = 'Subjects'
        subject_model = self.get_model()
        self.table_name = 'Assistance_records'
        assistance_model = self.get_model()

        for assistant in assistants:
            table_item = {'Nombre': assistant.name, 'Correo': assistant.email, 'Programa': program_model.get_by_id(
                assistant.program_id).program_name if program_model.get_by_id(
                assistant.program_id) is not None else None, 'Asignatura': subject_model.get_by_id(
                assistant.subject_id).subject_name if subject_model.get_by_id(
                assistant.subject_id) is not None else None}

            for event in events:
                date = event.event_date.strftime("%Y-%m-%d")
                table_item[date] = assistance_model.exist_record(event.id, assistant.id)

            data_result.append(table_item)

        return data_result

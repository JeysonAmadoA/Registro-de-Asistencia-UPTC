from Services.Implementation.Index_data_Service import Index_data_Service
from Services.Implementation.Data_store_Service import Data_store_Service


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('Hola')


    # Define los datos de ejemplo para cada tabla
    data_subjects = {'subject_name': 'Matemáticas'}
    Data_store_Service('Subjects').create_instance(data_subjects)

    data_programs = {'program_name': 'Ingeniería Informática'}
    Data_store_Service('Programs').create_instance(data_programs)

    data_events = {'event_date': '2023-09-25'}
    Data_store_Service('Events').create_instance(data_events)

    subject_id = Index_data_Service('Subjects').get_model().filter_by_subject_name('Matemáticas').id
    program_id = Index_data_Service('Programs').get_model().filter_by_program_name('Ingeniería Informática').id

    data_assistants = {'email': 'example@example.com', 'name': 'John Doe', 'program_id': program_id, 'subject_id': subject_id}
    Data_store_Service('Assistants').create_instance(data_assistants)

    event_id = Index_data_Service('Events').get_model().filter_by_event_date('2023-09-25').id
    assistant_id = Index_data_Service('Assistants').get_model().filter_by_email('example@example.com').id

    data_assistance_records = {'event_id': event_id, 'assistant_id': assistant_id, 'duration_time': '2 horas',
                               'entry_hour': '2023-09-25 08:00:00', 'departure_hour': '2023-09-25 10:00:00'}

    Data_store_Service('Assistance_records').create_instance(data_assistance_records)


    #result = Index_data_Service('Subjects').get_model().filter_by_subject_name('prueba')
    #result = Global_Helpers.get_model('Subjects').filter_by_subject_name('prueba')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

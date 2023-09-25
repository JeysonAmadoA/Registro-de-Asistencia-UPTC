import importlib


def get_model(table_name):
    try:
        module = importlib.import_module(f'Models.{table_name}')
        return getattr(module, table_name)
    except ModuleNotFoundError:
        return None

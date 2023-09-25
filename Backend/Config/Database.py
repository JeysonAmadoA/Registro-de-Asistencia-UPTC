from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from decouple import config


class Database:
    __instance = None
    session = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        if Database.__instance is not None:
            raise Exception("Error al instanciar configuración")
        else:
            Database.__instance = self
            engine = create_engine(config('DATABASE_CONNECTION'))
            Session = sessionmaker(bind=engine)
            self.session = Session()


try:
    db = Database.get_instance()
    db.session.execute(text('SELECT 1'))
    print("La conexión a la base de datos fue exitosa.")
except Exception as e:
    print("Ocurrió un error al intentar conectarse a la base de datos:", e)

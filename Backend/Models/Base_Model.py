from sqlalchemy.orm import declarative_base
from Config.Database import Database

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    session = Database.get_instance().session

    def __init__(self):
        self.database = Database.get_instance()

    def get_session(self):
        return self.database.session

    def begin(self):
        self.get_session().begin()

    def store(self):
        self.get_session().add(self)

    def delete(self):
        self.get_session().delete(self)

    def commit(self):
        self.get_session().commit()

    def close(self):
        self.get_session().close()

    @classmethod
    def get_all(cls):
        return cls.get_session().query(cls).all()

    @classmethod
    def get_by_id(cls, _id):
        return cls.get_session().query(cls).get(_id)

    def bulk_insert(self, models):
        self.get_session().bulk_save_objects(models)
        self.get_session().commit()

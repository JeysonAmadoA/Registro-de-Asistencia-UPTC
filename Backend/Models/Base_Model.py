from sqlalchemy.orm import declarative_base
from Config.Database import Database

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    @staticmethod
    def get_db():
        return Database.get_instance()

    def store(self):
        db = self.get_db()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db = self.get_db()
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        db = cls.get_db()
        return db.session.query(cls).all()

    @classmethod
    def get_by_id(cls, id):
        db = cls.get_db()
        return db.session.query(cls).get(id)

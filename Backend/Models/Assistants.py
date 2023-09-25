from sqlalchemy import Column, Integer, String, ForeignKey, or_
from Models.Base_Model import BaseModel


class Assistants(BaseModel):
    __tablename__ = 'assistants'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=False)
    name = Column(String(250), unique=False)
    program_id = Column(Integer, ForeignKey('programs.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    def __init__(self, email=None, name=None, program_id=None, subject_id=None):
        self.email = email
        self.name = name
        self.program_id = program_id
        self.subject_id = subject_id

    def __repr__(self):
        return f"<Asistente '{self.email}', '{self.name}', {self.program_id}, {self.subject_id}>"

    @classmethod
    def filter_by_email(cls, email):
        db = cls.get_db()
        return db.session.query(cls).filter(or_(cls.email == email)).first()

    @classmethod
    def filter_by_name(cls, name):
        db = cls.get_db()
        return db.session.query(cls).filter(or_(cls.name == name)).first()

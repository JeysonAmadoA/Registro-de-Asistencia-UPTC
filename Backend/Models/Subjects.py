from sqlalchemy import Column, Integer, String, or_
from Models.Base_Model import BaseModel


class Subjects(BaseModel):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String(250), unique=True)

    def __init__(self, subject_name=None):
        super().__init__()
        self.subject_name = subject_name

    def __repr__(self):
        return f"<Asignatura '{self.id}', '{self.subject_name}'>"

    @classmethod
    def filter_by_subject_name(cls, subject_name):
        return cls.session.query(cls).filter(or_(cls.subject_name == subject_name)).first()


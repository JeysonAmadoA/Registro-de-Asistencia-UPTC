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
        super().__init__()
        self.email = email
        self.name = name
        self.program_id = program_id
        self.subject_id = subject_id

    def __repr__(self):
        return f"<Asistente '{self.email}', '{self.name}', {self.program_id}, {self.subject_id}>"

    @classmethod
    def filter_by_email(cls, email):
        return cls.session.query(cls).filter(or_(cls.email == email)).first()

    @classmethod
    def filter_by_name(cls, name):
        return cls.session.query(cls).filter(or_(cls.name == name)).first()

    @classmethod
    def filter_by_program_id(cls, program_id):
        return cls.session.query(cls).filter(cls.program_id == program_id).all()

    @classmethod
    def filter_where_not_in_programs(cls, program_exclude):
        return cls.session.query(cls).filter(
            or_(cls.program_id.is_(None), ~cls.program_id.in_(program_exclude))
        ).all()


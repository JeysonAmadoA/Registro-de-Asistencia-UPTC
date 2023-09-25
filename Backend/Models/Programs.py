from sqlalchemy import Column, Integer, String, or_
from Models.Base_Model import BaseModel


class Programs(BaseModel):
    __tablename__ = 'programs'

    id = Column(Integer, primary_key=True)
    program_name = Column(String(250), unique=True)

    def __init__(self, program_name=None):
        self.program_name = program_name

    def __repr__(self):
        return '<Programa %r>' % self.program_name

    @classmethod
    def filter_by_program_name(cls, program_name):
        db = cls.get_db()
        return db.session.query(cls).filter(or_(cls.program_name == program_name)).first()

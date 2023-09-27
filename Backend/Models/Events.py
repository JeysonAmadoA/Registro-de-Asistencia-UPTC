from sqlalchemy import Column, Integer, Date, or_
from Models.Base_Model import BaseModel


class Events(BaseModel):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_date = Column(Date)

    def __init__(self, event_date=None):
        super().__init__()
        self.event_date = event_date

    def __repr__(self):
        return '<Evento %r>' % self.event_date

    @classmethod
    def filter_by_event_date(cls, event_date):
        return cls.session.query(cls).filter(or_(cls.event_date == event_date)).first()

from sqlalchemy import Column, Integer, String, ForeignKey, Date, and_
from Models.Base_Model import BaseModel


class Assistance_records(BaseModel):
    __tablename__ = 'assistance_records'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    assistant_id = Column(Integer, ForeignKey('assistants.id'))
    duration_time = Column(String(250), unique=False)
    entry_hour = Column(Date)
    departure_hour = Column(Date)

    def __init__(self, event_id=None, assistant_id=None, duration_time=None, entry_hour=None, departure_hour=None):
        super().__init__()
        self.event_id = event_id
        self.assistant_id = assistant_id
        self.duration_time = duration_time
        self.entry_hour = entry_hour
        self.departure_hour = departure_hour

    def __repr__(self):
        return f"<Asistencia '{self.event_id}', '{self.assistant_id}'>"

    @classmethod
    def exist_record(cls, event_id, assistant_id):
        result = cls.session.query(cls).filter(and_(cls.event_id == event_id, cls.assistant_id == assistant_id)).first()
        return True if result else False

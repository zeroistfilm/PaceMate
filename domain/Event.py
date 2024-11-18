from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from domain.dataclasses.event_dataclass import Event as EventDataClass

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    description = Column(String)
    event_type = Column(String)  # 이벤트 유형
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String)
    max_participants = Column(String)

    def __init__(self, title: str, description: str, event_type: str, start_date: DateTime, end_date: DateTime, location: str, max_participants: int):
        self.title = title
        self.description = description
        self.event_type = event_type
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.max_participants = max_participants

    def to_dataclass(self) -> EventDataClass:
        """Event 엔티티를 Event dataclass로 변환합니다."""
        return EventDataClass(
            id=self.id,
            title=self.title,
            description=self.description,
            event_type=self.event_type,
            start_date=self.start_date,
            end_date=self.end_date,
            location=self.location,
            max_participants=self.max_participants
        ) 
from sqlalchemy.orm import Session
from domain.dataclasses.event_dataclass import Event
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class EventRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self):
        """이벤트 테이블 생성"""
        Event.__table__.create(bind=self.db.get_bind(), checkfirst=True)

    def add_event(self, event: Event) -> Event:
        """이벤트를 데이터베이스에 추가합니다."""
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event

    def get_event(self, event_id: str) -> Event:
        """ID로 이벤트를 조회합니다."""
        return self.db.query(Event).filter(Event.id == event_id).first()

    def transform_event_data(self, event_data: dict) -> Event:
        """딕셔너리 형태의 이벤트 데이터를 Event dataclass로 변환합니다."""
        return Event(
            id=event_data.get("id", uuid.uuid4()),
            title=event_data["title"],
            description=event_data["description"],
            event_type=event_data["event_type"],
            start_date=event_data["start_date"],
            end_date=event_data["end_date"],
            location=event_data["location"],
            max_participants=event_data["max_participants"]
        )
  
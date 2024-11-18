import pytest
from service.EventService import EventService
from domain.Event import Event
import uuid
from datetime import datetime

@pytest.fixture
def event_service():
    return EventService()

def test_create_event(event_service):
    # 이벤트 생성 테스트
    event = event_service.create_event(
        title="New Year Marathon",
        description="Join us for the New Year Marathon!",
        event_type="COMPETITION",
        start_date=datetime(2023, 1, 1, 9, 0),
        end_date=datetime(2023, 1, 1, 12, 0),
        location="Seoul",
        max_participants=100
    )
    assert isinstance(event, Event)
    assert event.title == "New Year Marathon"

def test_register_participant(event_service):
    # 참가자 등록 테스트
    event = event_service.create_event(
        title="New Year Marathon",
        description="Join us for the New Year Marathon!",
        event_type="COMPETITION",
        start_date=datetime(2023, 1, 1, 9, 0),
        end_date=datetime(2023, 1, 1, 12, 0),
        location="Seoul",
        max_participants=100
    )
    result = event_service.register_participant(event.id, uuid.uuid4(), uuid.uuid4())
    assert result is not None 
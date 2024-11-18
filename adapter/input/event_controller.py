from fastapi import APIRouter, HTTPException
from service.EventService import EventService
from domain.dataclasses.event_dataclass import Event
from pydantic import BaseModel
import uuid
from datetime import datetime

router = APIRouter()
event_service = EventService()

class EventCreate(BaseModel):
    title: str
    description: str
    event_type: str
    start_date: datetime
    end_date: datetime
    location: str
    max_participants: int

@router.post("/events/")
def create_event(event: EventCreate):
    event = event_service.create_event(
        title=event.title,
        description=event.description,
        event_type=event.event_type,
        start_date=event.start_date,
        end_date=event.end_date,
        location=event.location,
        max_participants=event.max_participants
    )
    return event

@router.get("/events/{event_id}")
def read_event(event_id: str):
    event = event_service.get_event(uuid.UUID(event_id))
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event 
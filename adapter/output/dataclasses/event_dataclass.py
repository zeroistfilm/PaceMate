from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import List, Optional

@dataclass
class EventRegistration:
    user_id: uuid.UUID
    ticket_id: uuid.UUID
    registration_time: datetime

@dataclass
class Event:
    id: uuid.UUID
    title: str
    description: str
    event_type: str
    start_date: datetime
    end_date: datetime
    location: str
    max_participants: int
    registrations: List[EventRegistration] = None

    def __post_init__(self):
        if self.registrations is None:
            self.registrations = [] 
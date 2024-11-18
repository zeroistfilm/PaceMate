from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import List

@dataclass
class Challenge:
    id: uuid.UUID
    title: str
    description: str
    challenge_type: str
    status: str
    creator_id: uuid.UUID
    participants: List[uuid.UUID] = None
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if self.participants is None:
            self.participants = [] 
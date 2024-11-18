from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import List, Optional

@dataclass
class ClubMember:
    user_id: uuid.UUID
    role: str
    joined_at: datetime
    total_activities: int = 0
    total_distance: float = 0.0

@dataclass
class Club:
    id: uuid.UUID
    name: str
    description: str
    club_type: str
    visibility: str
    location: str
    members: List[ClubMember] = None
    created_at: datetime = datetime.now()

    def __post_init__(self):
        if self.members is None:
            self.members = [] 
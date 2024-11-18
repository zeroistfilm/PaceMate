from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import Dict, Any, Optional

@dataclass
class Notification:
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    body: str
    type: str
    priority: str
    status: str
    created_at: datetime
    scheduled_at: Optional[datetime] = None
    read_at: Optional[datetime] = None
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {} 
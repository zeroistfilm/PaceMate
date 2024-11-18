from dataclasses import dataclass
import uuid
from datetime import datetime

@dataclass
class User:
    id: uuid.UUID
    email: str
    username: str
    name: str
    birth_date: datetime
    gender: str 
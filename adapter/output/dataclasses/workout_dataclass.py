from dataclasses import dataclass
from datetime import datetime
from typing import List
import uuid

@dataclass
class TrackPoint:
    latitude: float
    longitude: float
    timestamp: datetime
    altitude: float
    heart_rate: int
    pace: float
    temperature: float

@dataclass
class Workout:
    id: uuid.UUID
    user_id: uuid.UUID
    workout_type: str
    start_time: datetime
    end_time: datetime
    distance: float
    duration: float
    track_points: List[TrackPoint] 
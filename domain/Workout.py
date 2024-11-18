from sqlalchemy import Column, String, Float, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from domain.dataclasses.workout_dataclass import Workout as WorkoutDataClass
from enum import Enum as PyEnum

Base = declarative_base()

class WorkoutType(PyEnum):
    RUNNING = "RUNNING"
    CYCLING = "CYCLING"
    WALKING = "WALKING"

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)  # 사용자 ID
    workout_type = Column(Enum(WorkoutType))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    distance = Column(Float)
    duration = Column(Float)

    def __init__(self, user_id: str, workout_type: WorkoutType, start_time: DateTime, end_time: DateTime, distance: float, duration: float):
        self.user_id = user_id
        self.workout_type = workout_type
        self.start_time = start_time
        self.end_time = end_time
        self.distance = distance
        self.duration = duration

    def to_dataclass(self) -> WorkoutDataClass:
        """Workout 엔티티를 Workout dataclass로 변환합니다."""
        return WorkoutDataClass(
            id=self.id,
            user_id=self.user_id,
            workout_type=self.workout_type,
            start_time=self.start_time,
            end_time=self.end_time,
            distance=self.distance,
            duration=self.duration,
            track_points=[]
        )


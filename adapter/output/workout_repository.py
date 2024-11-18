from sqlalchemy.orm import Session
from domain.dataclasses.workout_dataclass import Workout
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class WorkoutRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self):
        """운동 테이블 생성"""
        Workout.__table__.create(bind=self.db.get_bind(), checkfirst=True)

    def add_workout(self, workout: Workout) -> Workout:
        """운동을 데이터베이스에 추가합니다."""
        self.db.add(workout)
        self.db.commit()
        self.db.refresh(workout)
        return workout

    def get_workout(self, workout_id: str) -> Workout:
        """ID로 운동을 조회합니다."""
        return self.db.query(Workout).filter(Workout.id == workout_id).first()

    def transform_workout_data(self, workout_data: dict) -> Workout:
        """딕셔너리 형태의 운동 데이터를 Workout dataclass로 변환합니다."""
        return Workout(
            id=workout_data.get("id", uuid.uuid4()),
            user_id=workout_data["user_id"],
            workout_type=workout_data["workout_type"],
            start_time=workout_data["start_time"],
            end_time=workout_data["end_time"],
            distance=workout_data["distance"],
            duration=workout_data["duration"],
            track_points=[]
        ) 
from adapter.output.workout_repository import WorkoutRepository
from application.interfaces import IWorkoutService
from domain.dataclasses.workout_dataclass import Workout
import uuid
from sqlalchemy.orm import Session
from application.events import WorkoutDataCollectedEvent

class WorkoutService(IWorkoutService):
    def __init__(self, db: Session):
        self.workout_repository = WorkoutRepository(db)

    def create_workout(self, workout_data: dict) -> Workout:
        workout = self.workout_repository.transform_workout_data(workout_data)
        self.workout_repository.add_workout(workout)
        
        event = WorkoutCreatedEvent(workout_id=workout.id)
        publish_event(event)

        return workout

    def get_workout(self, workout_id: str) -> Workout:
        return self.workout_repository.get_workout(workout_id)

    def collect_workout_data(self, workout_data):
        self.workout_repository.save_workout_data(workout_data)
        
        # 운동 데이터 수집 이벤트 발행
        event = WorkoutDataCollectedEvent(workout_data=workout_data)
        publish_event(event)

    def save_workout_route(self, route_data):
        self.workout_repository.save_route_data(route_data)
        publish_event("WorkoutRouteSaved", route_data)

    def sync_workout_data(self, device_data):
        self.workout_repository.sync_data(device_data)
        publish_event("WorkoutDataSynced", device_data)

    def delete_workout(self, workout_id):
        self.workout_repository.delete_workout(workout_id)
        publish_event("WorkoutRecordDeleted", workout_id) 
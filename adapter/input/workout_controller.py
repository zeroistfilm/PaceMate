from fastapi import APIRouter, HTTPException
from service.WorkoutService import WorkoutService
from domain.dataclasses.workout_dataclass import Workout
from pydantic import BaseModel
import uuid

router = APIRouter()
workout_service = WorkoutService()

class WorkoutCreate(BaseModel):
    user_id: str
    workout_type: str
    start_time: str
    end_time: str
    distance: float
    duration: float

@router.post("/workouts/")
def create_workout(workout: WorkoutCreate):
    workout = workout_service.create_workout(
        user_id=uuid.UUID(workout.user_id),
        workout_type=workout.workout_type,
        start_time=workout.start_time,
        end_time=workout.end_time,
        distance=workout.distance,
        duration=workout.duration
    )
    return workout

@router.get("/workouts/{workout_id}")
def read_workout(workout_id: str):
    workout = workout_service.get_workout(uuid.UUID(workout_id))
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout 
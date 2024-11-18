import pytest
from service.WorkoutService import WorkoutService
from domain.Workout import Workout, TrackPoint
import uuid
from datetime import datetime

@pytest.fixture
def workout_service():
    return WorkoutService()

def test_create_workout(workout_service):
    # 운동 생성 테스트
    workout = workout_service.create_workout(
        user_id=uuid.uuid4(),
        workout_type="RUNNING",
        start_time="2023-01-01T10:00:00",
        end_time="2023-01-01T11:00:00",
        distance=5.0,
        duration=60.0
    )
    assert isinstance(workout, Workout)
    assert workout.distance == 5.0

def test_add_track_point(workout_service):
    # 트랙 포인트 추가 테스트
    workout = workout_service.create_workout(
        user_id=uuid.uuid4(),
        workout_type="RUNNING",
        start_time="2023-01-01T10:00:00",
        end_time="2023-01-01T11:00:00",
        distance=5.0,
        duration=60.0
    )
    track_point = TrackPoint(latitude=37.5665, longitude=126.9780, timestamp="2023-01-01T10:05:00", altitude=10.0, heart_rate=150, pace=5.0, temperature=25.0)
    workout_service.add_track_point(workout.id, track_point)
    assert len(workout.track_points) == 1

def test_calculate_summary(workout_service):
    # 운동 요약 계산 테스트
    workout = workout_service.create_workout(
        user_id=uuid.uuid4(),
        workout_type="RUNNING",
        start_time="2023-01-01T10:00:00",
        end_time="2023-01-01T11:00:00",
        distance=5.0,
        duration=60.0
    )
    track_point1 = TrackPoint(latitude=37.5665, longitude=126.9780, timestamp="2023-01-01T10:00:00", altitude=10.0, heart_rate=150, pace=5.0, temperature=25.0)
    track_point2 = TrackPoint(latitude=37.5665, longitude=126.9780, timestamp="2023-01-01T10:30:00", altitude=20.0, heart_rate=160, pace=4.5, temperature=26.0)
    workout_service.add_track_point(workout.id, track_point1)
    workout_service.add_track_point(workout.id, track_point2)
    
    summary = workout_service.calculate_summary(workout.id)
    assert summary.avg_heart_rate is not None  # 평균 심박수가 계산되었는지 확인
    assert summary.calories == int(workout.distance * (workout.user.weight * 0.9))  # 칼로리 계산 확인
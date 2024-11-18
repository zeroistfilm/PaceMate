import pytest
from service.UserService import UserService
from domain.dataclasses.user_dataclass import User
import uuid
from datetime import datetime

@pytest.fixture
def user_service():
    return UserService()

def test_register_user(user_service):
    # 사용자 등록 테스트
    user = user_service.register_user(
        email="test@example.com",
        username="testuser",
        password_hash="hashedpassword",
        name="Test User",
        birth_date=datetime(1990, 1, 1),
        gender="MALE"
    )
    assert isinstance(user, User)
    assert user.email == "test@example.com"

def test_add_health_metrics(user_service):
    # 건강 지표 추가 테스트
    user = user_service.register_user(
        email="test@example.com",
        username="testuser",
        password_hash="hashedpassword",
        name="Test User",
        birth_date=datetime(1990, 1, 1),
        gender="MALE"
    )
    metrics = HealthMetrics(height=180, weight=75)
    user_service.add_health_metrics(user.id, metrics)
    assert len(user.health_metrics) == 1

def test_add_workout_goal(user_service):
    # 운동 목표 추가 테스트
    user = user_service.register_user(
        email="test@example.com",
        username="testuser",
        password_hash="hashedpassword",
        name="Test User",
        birth_date=datetime(1990, 1, 1),
        gender="MALE"
    )
    goal = WorkoutGoal(goal_type="DISTANCE", target_value=5.0, start_date="2023-01-01", end_date="2023-01-31")
    user_service.add_workout_goal(user.id, goal)
    assert len(user.workout_goals) == 1

def test_update_user_stats(user_service):
    # 사용자 통계 업데이트 테스트
    user = user_service.register_user(
        email="test@example.com",
        username="testuser",
        password_hash="hashedpassword",
        name="Test User",
        birth_date=datetime(1990, 1, 1),
        gender="MALE"
    )
    user_service.update_user_stats(user.id, distance=5.0, duration=30.0, calories=300, pace=6.0, elevation=10.0)
    assert user.stats.total_distance == 5.0
    assert user.stats.total_workouts == 1 
import pytest
from service.ChallengeService import ChallengeService
from domain.Challenge import Challenge
import uuid

@pytest.fixture
def challenge_service():
    return ChallengeService()

def test_create_challenge(challenge_service):
    # 챌린지 생성 테스트
    challenge = challenge_service.create_challenge(
        title="January Running Challenge",
        description="Run 100 km in January",
        challenge_type="DISTANCE",
        rules={"min_participants": 5, "max_participants": 50, "start_date": "2023-01-01", "end_date": "2023-01-31", "target_value": 100}
    )
    assert isinstance(challenge, Challenge)
    assert challenge.title == "January Running Challenge"

def test_add_participant(challenge_service):
    # 참가자 추가 테스트
    challenge = challenge_service.create_challenge(
        title="January Running Challenge",
        description="Run 100 km in January",
        challenge_type="DISTANCE",
        rules={"min_participants": 5, "max_participants": 50, "start_date": "2023-01-01", "end_date": "2023-01-31", "target_value": 100}
    )
    result = challenge_service.add_participant(challenge.id, uuid.uuid4())
    assert result is True

def test_get_rankings(challenge_service):
    # 순위 조회 테스트
    challenge = challenge_service.create_challenge(
        title="January Running Challenge",
        description="Run 100 km in January",
        challenge_type="DISTANCE",
        rules={"min_participants": 5, "max_participants": 50, "start_date": "2023-01-01", "end_date": "2023-01-31", "target_value": 100}
    )
    challenge.add_participant(uuid.uuid4())  # 참가자 추가
    rankings = challenge_service.get_rankings(challenge.id)
    assert len(rankings) == 1  # 참가자가 추가되었으므로 순위가 1명이어야 함
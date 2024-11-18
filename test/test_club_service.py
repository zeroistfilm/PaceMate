import pytest
from service.ClubService import ClubService
from domain.Club import Club
import uuid

@pytest.fixture
def club_service():
    return ClubService()

def test_create_club(club_service):
    # 클럽 생성 테스트
    club = club_service.create_club(
        name="Running Club",
        description="A club for running enthusiasts",
        club_type="RUNNING",
        visibility="PUBLIC",
        location="Seoul"
    )
    assert isinstance(club, Club)
    assert club.name == "Running Club"

def test_add_member(club_service):
    # 회원 추가 테스트
    club = club_service.create_club(
        name="Running Club",
        description="A club for running enthusiasts",
        club_type="RUNNING",
        visibility="PUBLIC",
        location="Seoul"
    )
    result = club_service.add_member(club.id, uuid.uuid4(), "MEMBER")
    assert result is True

def test_remove_member(club_service):
    # 회원 제거 테스트
    club = club_service.create_club(
        name="Running Club",
        description="A club for running enthusiasts",
        club_type="RUNNING",
        visibility="PUBLIC",
        location="Seoul"
    )
    user_id = uuid.uuid4()
    club_service.add_member(club.id, user_id, "MEMBER")
    result = club_service.remove_member(club.id, user_id)
    assert result is True 
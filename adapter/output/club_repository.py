from sqlalchemy.orm import Session
from adapter.output.dataclasses.club_dataclass import Club
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class ClubRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self):
        """클럽 테이블 생성"""
        Club.__table__.create(bind=self.db.get_bind(), checkfirst=True)

    def add_club(self, club: Club) -> Club:
        """클럽을 데이터베이스에 추가합니다."""
        self.db.add(club)
        self.db.commit()
        self.db.refresh(club)
        return club

    def get_club(self, club_id: str) -> Club:
        """ID로 클럽을 조회합니다."""
        return self.db.query(Club).filter(Club.id == club_id).first()

    def transform_club_data(self, club_data: dict) -> Club:
        """딕셔너리 형태의 클럽 데이터를 Club dataclass로 변환합니다."""
        return Club(
            id=club_data.get("id", uuid.uuid4()),
            name=club_data["name"],
            description=club_data["description"],
            club_type=club_data["club_type"],
            visibility=club_data["visibility"],
            location=club_data["location"]
        )
  
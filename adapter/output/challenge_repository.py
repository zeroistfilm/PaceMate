from sqlalchemy.orm import Session
from domain.dataclasses.challenge_dataclass import Challenge
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class ChallengeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self):
        """챌린지 테이블 생성"""
        Challenge.__table__.create(bind=self.db.get_bind(), checkfirst=True)

    def add_challenge(self, challenge: Challenge) -> Challenge:
        """챌린지를 데이터베이스에 추가합니다."""
        self.db.add(challenge)
        self.db.commit()
        self.db.refresh(challenge)
        return challenge

    def get_challenge(self, challenge_id: str) -> Challenge:
        """ID로 챌린지를 조회합니다."""
        return self.db.query(Challenge).filter(Challenge.id == challenge_id).first()

    def transform_challenge_data(self, challenge_data: dict) -> Challenge:
        """딕셔너리 형태의 챌린지 데이터를 Challenge dataclass로 변환합니다."""
        return Challenge(
            id=challenge_data.get("id", uuid.uuid4()),
            title=challenge_data["title"],
            description=challenge_data["description"],
            challenge_type=challenge_data["challenge_type"],
            status="DRAFT",
            creator_id=challenge_data["creator_id"],
            rules=challenge_data["rules"]
        )
  
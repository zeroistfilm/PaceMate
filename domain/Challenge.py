from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from domain.dataclasses.challenge_dataclass import Challenge as ChallengeDataClass
from enum import Enum as PyEnum

Base = declarative_base()

class ChallengeType(PyEnum):
    DISTANCE = "DISTANCE"
    TIME = "TIME"
    FREQUENCY = "FREQUENCY"

class ChallengeStatus(PyEnum):
    DRAFT = "DRAFT"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    description = Column(String)
    challenge_type = Column(Enum(ChallengeType))
    status = Column(Enum(ChallengeStatus))
    creator_id = Column(String)  # 생성자 ID
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, title: str, description: str, challenge_type: ChallengeType, creator_id: str):
        self.title = title
        self.description = description
        self.challenge_type = challenge_type
        self.status = ChallengeStatus.DRAFT
        self.creator_id = creator_id

    def to_dataclass(self) -> ChallengeDataClass:
        """Challenge 엔티티를 Challenge dataclass로 변환합니다."""
        return ChallengeDataClass(
            id=self.id,
            title=self.title,
            description=self.description,
            challenge_type=self.challenge_type,
            status=self.status,
            creator_id=self.creator_id,
            created_at=self.created_at
        ) 
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from domain.dataclasses.club_dataclass import Club as ClubDataClass

Base = declarative_base()

class Club(Base):
    __tablename__ = "clubs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    description = Column(String)
    club_type = Column(String)  # 클럽 유형
    visibility = Column(String)  # 공개 설정
    location = Column(String)    # 활동 지역
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name: str, description: str, club_type: str, visibility: str, location: str):
        self.name = name
        self.description = description
        self.club_type = club_type
        self.visibility = visibility
        self.location = location

    def to_dataclass(self) -> ClubDataClass:
        """Club 엔티티를 Club dataclass로 변환합니다."""
        return ClubDataClass(
            id=self.id,
            name=self.name,
            description=self.description,
            club_type=self.club_type,
            visibility=self.visibility,
            location=self.location,
            created_at=self.created_at
        ) 
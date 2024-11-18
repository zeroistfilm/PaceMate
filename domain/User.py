from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from domain.dataclasses.user_dataclass import User as UserDataClass
from enum import Enum as PyEnum

Base = declarative_base()

class Gender(PyEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class ActivityLevel(PyEnum):
    SEDENTARY = "SEDENTARY"
    LIGHTLY_ACTIVE = "LIGHTLY_ACTIVE"
    MODERATELY_ACTIVE = "MODERATELY_ACTIVE"
    VERY_ACTIVE = "VERY_ACTIVE"
    EXTRA_ACTIVE = "EXTRA_ACTIVE"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    birth_date = Column(DateTime)
    gender = Column(Enum(Gender))
    join_date = Column(DateTime, default=datetime.utcnow)
    activity_level = Column(Enum(ActivityLevel))

    def __init__(self, email: str, username: str, password_hash: str, name: str, birth_date: datetime, gender: Gender, activity_level: ActivityLevel):
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.activity_level = activity_level

    def to_dataclass(self) -> UserDataClass:
        """User 엔티티를 User dataclass로 변환합니다."""
        return UserDataClass(
            id=self.id,
            email=self.email,
            username=self.username,
            name=self.name,
            birth_date=self.birth_date,
            gender=self.gender,
            join_date=self.join_date,
            activity_level=self.activity_level
        )

    def calculate_age(self) -> int:
        """사용자의 나이를 계산하는 메서드"""
        today = datetime.now()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
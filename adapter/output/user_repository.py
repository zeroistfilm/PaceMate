from sqlalchemy.orm import Session
from adapter.output.dataclasses.user_dataclass import User
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self):
        """사용자 테이블 생성"""
        User.__table__.create(bind=self.db.get_bind(), checkfirst=True)

    def add_user(self, user: User) -> User:
        """사용자를 데이터베이스에 추가합니다."""
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: str) -> User:
        """ID로 사용자를 조회합니다."""
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user: User) -> User:
        """사용자 정보를 업데이트합니다."""
        existing_user = self.get_user(user.id)
        if existing_user:
            existing_user.email = user.email
            existing_user.username = user.username
            existing_user.name = user.name
            existing_user.birth_date = user.birth_date
            existing_user.gender = user.gender
            self.db.commit()
            self.db.refresh(existing_user)
            return existing_user
        return None

    def delete_user(self, user_id: str) -> bool:
        """사용자를 데이터베이스에서 삭제합니다."""
        user = self.get_user(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def transform_user_data(self, user_data: dict) -> User:
        """딕셔너리 형태의 사용자 데이터를 User dataclass로 변환합니다."""
        return User(
            id=user_data.get("id", uuid.uuid4()),
            email=user_data["email"],
            username=user_data["username"],
            name=user_data["name"],
            birth_date=user_data["birth_date"],
            gender=user_data["gender"]
        ) 
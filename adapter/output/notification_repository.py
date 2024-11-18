from sqlalchemy.orm import Session
from domain.dataclasses.notification_dataclass import Notification
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class NotificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_table(self):
        """알림 테이블 생성"""
        Notification.__table__.create(bind=self.db.get_bind(), checkfirst=True)

    def add_notification(self, notification: Notification) -> Notification:
        """알림을 데이터베이스에 추가합니다."""
        self.db.add(notification)
        self.db.commit()
        self.db.refresh(notification)
        return notification

    def get_notification(self, notification_id: str) -> Notification:
        """ID로 알림을 조회합니다."""
        return self.db.query(Notification).filter(Notification.id == notification_id).first()

    def transform_notification_data(self, notification_data: dict) -> Notification:
        """딕셔너리 형태의 알림 데이터를 Notification dataclass로 변환합니다."""
        return Notification(
            id=notification_data.get("id", uuid.uuid4()),
            user_id=notification_data["user_id"],
            title=notification_data["title"],
            body=notification_data["body"],
            type=notification_data["type"],
            priority=notification_data["priority"],
            status=notification_data["status"],
            created_at=notification_data.get("created_at", datetime.now())
        )
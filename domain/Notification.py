from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from domain.dataclasses.notification_dataclass import Notification as NotificationDataClass

Base = declarative_base()

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)  # 수신자 ID
    title = Column(String)
    body = Column(String)
    type = Column(String)  # 알림 유형
    priority = Column(String)  # 우선순위
    status = Column(String)  # 상태
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, user_id: str, title: str, body: str, notification_type: str, priority: str):
        self.user_id = user_id
        self.title = title
        self.body = body
        self.type = notification_type
        self.priority = priority
        self.status = "PENDING"

    def to_dataclass(self) -> NotificationDataClass:
        """Notification 엔티티를 Notification dataclass로 변환합니다."""
        return NotificationDataClass(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            body=self.body,
            type=self.type,
            priority=self.priority,
            status=self.status,
            created_at=self.created_at
        )
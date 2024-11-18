from adapter.output.notification_repository import NotificationRepository
from domain.dataclasses.notification_dataclass import Notification
import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from application.events import UserCreatedEvent

class NotificationService:
    def __init__(self, db: Session):
        self.notification_repository = NotificationRepository(db)

    def create_notification(self, user_id: uuid.UUID, title: str, body: str, notification_type: str) -> Notification:
        notification = Notification(
            id=uuid.uuid4(),
            user_id=user_id,
            title=title,
            body=body,
            type=notification_type,
            priority="MEDIUM",
            status="PENDING",
            created_at=datetime.now()
        )
        return self.notification_repository.add_notification(notification)

    def handle_user_created_event(self, event: UserCreatedEvent):
        title = "환영합니다!"
        body = f"안녕하세요 {event.username}님, 저희 플랫폼에 오신 것을 환영합니다!"
        self.create_notification(event.user_id, title, body, "WELCOME")

    def send_notification(self, notification_data):
        publish_event("NotificationSent", notification_data)
        event = NotificationSentEvent(notification_data=notification_data)
        publish_event(event)

    def follow_event(self, event_id):
        publish_event("EventFollowed", event_id)

    def mark_notification_as_read(self, notification_id):
        publish_event("NotificationRead", notification_id) 
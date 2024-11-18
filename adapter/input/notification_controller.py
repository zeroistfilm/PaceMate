from fastapi import APIRouter, HTTPException
from service.NotificationService import NotificationService
from domain.dataclasses.notification_dataclass import Notification
from pydantic import BaseModel
import uuid

router = APIRouter()
notification_service = NotificationService()

class NotificationCreate(BaseModel):
    user_id: str
    title: str
    body: str
    notification_type: str

@router.post("/notifications/")
def create_notification(notification: NotificationCreate):
    notification = notification_service.create_notification(
        user_id=uuid.UUID(notification.user_id),
        title=notification.title,
        body=notification.body,
        notification_type=notification.notification_type
    )
    return notification

@router.get("/notifications/{notification_id}")
def read_notification(notification_id: str):
    notification = notification_service.get_notification(uuid.UUID(notification_id))
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification 
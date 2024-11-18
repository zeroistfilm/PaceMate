import pytest
from service.NotificationService import NotificationService
from domain.Notification import Notification
import uuid

@pytest.fixture
def notification_service():
    return NotificationService()

def test_create_notification(notification_service):
    # 알림 생성 테스트
    notification = notification_service.create_notification(
        user_id=uuid.uuid4(),
        title="Test Notification",
        body="This is a test notification.",
        notification_type="WORKOUT"
    )
    assert isinstance(notification, Notification)
    assert notification.title == "Test Notification"

def test_mark_as_read(notification_service):
    # 알림 읽음 처리 테스트
    notification = notification_service.create_notification(
        user_id=uuid.uuid4(),
        title="Test Notification",
        body="This is a test notification.",
        notification_type="WORKOUT"
    )
    notification_service.mark_as_read(notification.id)
    assert notification.status == "READ" 
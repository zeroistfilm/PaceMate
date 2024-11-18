from adapter.output.user_repository import UserRepository
from application.interfaces import IUserService
from application.events import UserCreatedEvent
from domain.dataclasses.user_dataclass import User
from domain.UserModel import UserModel
import uuid
from sqlalchemy.orm import Session

class UserService(IUserService):
    def __init__(self, db: Session, event_publisher):
        self.user_repository = UserRepository(db)
        self.event_publisher = event_publisher

    def register_user(self, user_data: dict) -> UserModel:
        user = self.user_repository.transform_user_data(user_data)
        self.user_repository.add_user(user)

        event = UserCreatedEvent(user_id=user.id, email=user.email, username=user.username)
        self.event_publisher.publish(event)

        return UserModel(user)

    def login_user(self, credentials):
        user = self.user_repository.authenticate_user(credentials)
        if user:
            publish_event("UserLoggedIn", user.id)
            return UserModel(user)
        raise Exception("Invalid credentials")

    def update_user_profile(self, user_id, updated_data):
        self.user_repository.update_user(user_id, updated_data)
        publish_event("UserProfileUpdated", user_id, updated_data)

    def change_user_password(self, user_id, new_password):
        self.user_repository.update_password(user_id, new_password)
        publish_event("UserPasswordChanged", user_id)

    def delete_user(self, user_id):
        self.user_repository.delete_user(user_id)
        publish_event("UserDeleted", user_id) 
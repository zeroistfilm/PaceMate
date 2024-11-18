from application.UserService import UserService
from application.WorkoutService import WorkoutService
from application.ChallengeService import ChallengeService
from application.CommunityService import CommunityService
from application.NotificationService import NotificationService
from application.DataVisualizationService import DataVisualizationService
from application.events import (
    UserCreatedEvent,
    UserLoggedInEvent,
    UserProfileUpdatedEvent,
    UserPasswordChangedEvent,
    UserDeletedEvent,
    WorkoutCreatedEvent,
    WorkoutDataCollectedEvent,
    WorkoutRouteSavedEvent,
    WorkoutDataSyncedEvent,
    WorkoutRecordDeletedEvent,
    ChallengeCreatedEvent,
    ChallengeJoinedEvent,
    ChallengeRecordUpdatedEvent,
    ChallengeEndedEvent,
    PostCreatedEvent,
    CommentCreatedEvent,
    PostUpdatedEvent,
    PostDeletedEvent,
    CommentDeletedEvent,
    NotificationSentEvent,
    NotificationReadEvent,
    WorkoutDataVisualizedEvent
)

class EventHandler:
    def __init__(self, user_service: UserService, workout_service: WorkoutService,
                 challenge_service: ChallengeService, community_service: CommunityService,
                 notification_service: NotificationService, data_visualization_service: DataVisualizationService):
        self.user_service = user_service
        self.workout_service = workout_service
        self.challenge_service = challenge_service
        self.community_service = community_service
        self.notification_service = notification_service
        self.data_visualization_service = data_visualization_service

    def handle_user_created(self, event: UserCreatedEvent):
        print(f"User created: {event.username}")
        self.notification_service.handle_user_created_event(event)

    def handle_user_logged_in(self, event: UserLoggedInEvent):
        print(f"User logged in: {event.user_id}")

    def handle_user_profile_updated(self, event: UserProfileUpdatedEvent):
        print(f"User profile updated: {event.user_id}, Data: {event.updated_data}")

    def handle_user_password_changed(self, event: UserPasswordChangedEvent):
        print(f"User password changed: {event.user_id}")

    def handle_user_deleted(self, event: UserDeletedEvent):
        print(f"User deleted: {event.user_id}")

    def handle_workout_created(self, event: WorkoutCreatedEvent):
        print(f"Workout created: {event.workout_id}")

    def handle_workout_data_collected(self, event: WorkoutDataCollectedEvent):
        print(f"Workout data collected: {event.workout_data}")

    def handle_workout_route_saved(self, event: WorkoutRouteSavedEvent):
        print(f"Workout route saved: {event.route_data}")

    def handle_workout_data_synced(self, event: WorkoutDataSyncedEvent):
        print(f"Workout data synced: {event.device_data}")

    def handle_workout_record_deleted(self, event: WorkoutRecordDeletedEvent):
        print(f"Workout record deleted: {event.workout_id}")

    def handle_challenge_created(self, event: ChallengeCreatedEvent):
        print(f"Challenge created: {event.challenge_data}")

    def handle_challenge_joined(self, event: ChallengeJoinedEvent):
        print(f"User {event.user_id} joined challenge {event.challenge_id}")

    def handle_challenge_record_updated(self, event: ChallengeRecordUpdatedEvent):
        print(f"Challenge record updated for user {event.user_id} in challenge {event.challenge_id}")

    def handle_challenge_ended(self, event: ChallengeEndedEvent):
        print(f"Challenge ended: {event.challenge_id}")

    def handle_post_created(self, event: PostCreatedEvent):
        print(f"Post created: {event.post_data}")

    def handle_comment_created(self, event: CommentCreatedEvent):
        print(f"Comment created: {event.comment_data}")

    def handle_post_updated(self, event: PostUpdatedEvent):
        print(f"Post updated: {event.post_id}, Data: {event.updated_data}")

    def handle_post_deleted(self, event: PostDeletedEvent):
        print(f"Post deleted: {event.post_id}")

    def handle_comment_deleted(self, event: CommentDeletedEvent):
        print(f"Comment deleted: {event.comment_id}")

    def handle_notification_sent(self, event: NotificationSentEvent):
        print(f"Notification sent: {event.notification_data}")

    def handle_notification_read(self, event: NotificationReadEvent):
        print(f"Notification read: {event.notification_id}")

    def handle_workout_data_visualized(self, event: WorkoutDataVisualizedEvent):
        print(f"Workout data visualized for user: {event.user_id}")

    # 추가적인 이벤트 핸들러를 여기에 추가
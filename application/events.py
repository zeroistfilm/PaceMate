class UserCreatedEvent:
    def __init__(self, user_id, email, username):
        self.user_id = user_id  # 사용자 ID
        self.email = email  # 사용자 이메일
        self.username = username  # 사용자 이름

class UserLoggedInEvent:
    def __init__(self, user_id):
        self.user_id = user_id  # 로그인한 사용자 ID

class UserProfileUpdatedEvent:
    def __init__(self, user_id, updated_data):
        self.user_id = user_id  # 업데이트된 사용자 ID
        self.updated_data = updated_data  # 업데이트된 데이터

class UserPasswordChangedEvent:
    def __init__(self, user_id):
        self.user_id = user_id  # 비밀번호가 변경된 사용자 ID

class UserDeletedEvent:
    def __init__(self, user_id):
        self.user_id = user_id  # 삭제된 사용자 ID

class WorkoutCreatedEvent:
    def __init__(self, workout_id):
        self.workout_id = workout_id  # 생성된 운동 ID

class WorkoutDataCollectedEvent:
    def __init__(self, workout_data):
        self.workout_data = workout_data  # 수집된 운동 데이터

class WorkoutRouteSavedEvent:
    def __init__(self, route_data):
        self.route_data = route_data  # 저장된 운동 경로 데이터

class WorkoutDataSyncedEvent:
    def __init__(self, device_data):
        self.device_data = device_data  # 동기화된 기기 데이터

class WorkoutRecordDeletedEvent:
    def __init__(self, workout_id):
        self.workout_id = workout_id  # 삭제된 운동 ID

class ChallengeCreatedEvent:
    def __init__(self, challenge_data):
        self.challenge_data = challenge_data  # 생성된 챌린지 데이터

class ChallengeJoinedEvent:
    def __init__(self, user_id, challenge_id):
        self.user_id = user_id  # 챌린지에 참여한 사용자 ID
        self.challenge_id = challenge_id  # 참여한 챌린지 ID

class ChallengeRecordUpdatedEvent:
    def __init__(self, user_id, challenge_id, record_data):
        self.user_id = user_id  # 업데이트된 사용자 ID
        self.challenge_id = challenge_id  # 업데이트된 챌린지 ID
        self.record_data = record_data  # 업데이트된 기록 데이터

class ChallengeEndedEvent:
    def __init__(self, challenge_id):
        self.challenge_id = challenge_id  # 종료된 챌린지 ID

class PostCreatedEvent:
    def __init__(self, post_data):
        self.post_data = post_data  # 생성된 게시글 데이터

class CommentCreatedEvent:
    def __init__(self, comment_data):
        self.comment_data = comment_data  # 생성된 댓글 데이터

class PostUpdatedEvent:
    def __init__(self, post_id, updated_data):
        self.post_id = post_id  # 업데이트된 게시글 ID
        self.updated_data = updated_data  # 업데이트된 데이터

class PostDeletedEvent:
    def __init__(self, post_id):
        self.post_id = post_id  # 삭제된 게시글 ID

class CommentDeletedEvent:
    def __init__(self, comment_id):
        self.comment_id = comment_id  # 삭제된 댓글 ID

class NotificationSentEvent:
    def __init__(self, notification_data):
        self.notification_data = notification_data  # 전송된 알림 데이터

class NotificationReadEvent:
    def __init__(self, notification_id):
        self.notification_id = notification_id  # 읽은 알림 ID

class WorkoutDataVisualizedEvent:
    def __init__(self, user_id):
        self.user_id = user_id  # 데이터 시각화된 사용자 ID

# 추가적인 이벤트 정의
class ChallengeReminderEvent:
    def __init__(self, user_id, challenge_id):
        self.user_id = user_id  # 챌린지 알림을 받을 사용자 ID
        self.challenge_id = challenge_id  # 알림을 받을 챌린지 ID

class WeeklySummaryEvent:
    def __init__(self, user_id, summary_data):
        self.user_id = user_id  # 주간 요약을 받을 사용자 ID
        self.summary_data = summary_data  # 주간 요약 데이터

class GoalAchievedEvent:
    def __init__(self, user_id, goal_data):
        self.user_id = user_id  # 목표를 달성한 사용자 ID
        self.goal_data = goal_data  # 달성한 목표 데이터
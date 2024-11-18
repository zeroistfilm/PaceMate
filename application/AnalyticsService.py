class AnalyticsService:
    def track_user_creation(self, event: UserCreatedEvent):
        print(f"새 사용자 등록: {event.username} (ID: {event.user_id})")
        # 통계 데이터에 사용자 추가 로직 
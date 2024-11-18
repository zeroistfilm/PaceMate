from adapter.output.community_repository import CommunityRepository
from application.interfaces import ICommunityService
import uuid
from sqlalchemy.orm import Session
from application.events import PostCreatedEvent

class CommunityService(ICommunityService):
    def __init__(self, db: Session):
        self.community_repository = CommunityRepository(db)

    def create_post(self, post_data):
        post = self.community_repository.create_post(post_data)
        
        # 게시글 생성 이벤트 발행
        event = PostCreatedEvent(post_data=post)
        publish_event(event)

    def create_comment(self, comment_data):
        comment = self.community_repository.create_comment(comment_data)
        publish_event("CommentCreated", comment)

    def update_post(self, post_id, updated_data):
        self.community_repository.update_post(post_id, updated_data)
        publish_event("PostUpdated", post_id, updated_data)

    def delete_post(self, post_id):
        self.community_repository.delete_post(post_id)
        publish_event("PostDeleted", post_id)

    def delete_comment(self, comment_id):
        self.community_repository.delete_comment(comment_id)
        publish_event("CommentDeleted", comment_id) 
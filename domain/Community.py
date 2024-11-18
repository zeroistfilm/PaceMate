from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import uuid

class PostType(Enum):
    GENERAL = "GENERAL"          # 일반 게시글
    MARKET = "MARKET"            # 중고 거래
    REVIEW = "REVIEW"            # 제품 리뷰
    EVENT = "EVENT"              # 이벤트/대회
    NOTICE = "NOTICE"            # 공지사항
    PROMOTION = "PROMOTION"      # 업체 홍보

class PostStatus(Enum):
    DRAFT = "DRAFT"              # 임시저장
    PUBLISHED = "PUBLISHED"      # 게시됨
    HIDDEN = "HIDDEN"            # 숨김
    DELETED = "DELETED"          # 삭제됨

@dataclass
class Comment:
    id: uuid.UUID               # 댓글 ID
    post_id: uuid.UUID          # 게시글 ID
    user_id: uuid.UUID          # 작성자 ID
    content: str                # 내용
    created_at: datetime        # 작성일시
    updated_at: datetime        # 수정일시
    parent_id: Optional[uuid.UUID] = None  # 부모 댓글 ID (대댓글용)
    is_deleted: bool = False    # 삭제 여부

@dataclass
class Attachment:
    id: uuid.UUID               # 첨부파일 ID
    file_name: str              # 파일명
    file_type: str              # 파일 타입
    file_size: int              # 파일 크기
    file_url: str              # 파일 URL
    uploaded_at: datetime       # 업로드 일시

@dataclass
class CommunityPost:
    id: uuid.UUID               # 게시글 ID
    title: str                  # 제목
    content: str                # 내용
    author_id: uuid.UUID        # 작성자 ID
    post_type: PostType         # 게시글 유형
    status: PostStatus          # 상태
    created_at: datetime        # 작성일시
    updated_at: datetime        # 수정일시
    comments: List[Comment] = None  # 댓글 목록
    attachments: List[Attachment] = None  # 첨부파일 목록
    
    def __post_init__(self):
        if self.comments is None:
            self.comments = []
        if self.attachments is None:
            self.attachments = []

    def add_comment(self, user_id: uuid.UUID, content: str, 
                   parent_id: Optional[uuid.UUID] = None) -> Comment:
        """댓글 추가"""
        comment = Comment(
            id=uuid.uuid4(),
            post_id=self.id,
            user_id=user_id,
            content=content,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            parent_id=parent_id
        )
        self.comments.append(comment)
        return comment

    def add_attachment(self, file_name: str, file_type: str,
                      file_size: int, file_url: str) -> Attachment:
        """첨부파일 추가"""
        attachment = Attachment(
            id=uuid.uuid4(),
            file_name=file_name,
            file_type=file_type,
            file_size=file_size,
            file_url=file_url,
            uploaded_at=datetime.now()
        )
        self.attachments.append(attachment)
        return attachment

    def delete(self):
        """게시글 삭제"""
        self.status = PostStatus.DELETED
        self.updated_at = datetime.now()

@dataclass
class MarketPost:
    id: uuid.UUID               # 게시글 ID
    product: Product            # 상품 정보
    seller_id: uuid.UUID        # 판매자 ID
    created_at: datetime = datetime.now()  # 등록일
    updated_at: datetime = datetime.now()  # 수정일
    status: str = "ACTIVE"      # 상태 (ACTIVE, SOLD, DELETED)

    def mark_as_sold(self):
        """상품 판매 완료 처리"""
        self.status = "SOLD"
        self.updated_at = datetime.now()

    def delete(self):
        """게시글 삭제"""
        self.status = "DELETED"
        self.updated_at = datetime.now()

@dataclass
class Community:
    id: uuid.UUID               # 커뮤니티 ID
    posts: List[CommunityPost] = None  # 게시글 목록

    def __post_init__(self):
        if self.posts is None:
            self.posts = []

    def add_post(self, title: str, content: str, author_id: uuid.UUID, post_type: PostType) -> CommunityPost:
        """게시글 추가"""
        post = CommunityPost(
            id=uuid.uuid4(),
            title=title,
            content=content,
            author_id=author_id,
            post_type=post_type,
            status=PostStatus.DRAFT
        )
        self.posts.append(post)
        return post

    def get_active_posts(self) -> List[CommunityPost]:
        """활성 게시글 조회"""
        return [post for post in self.posts if post.status == PostStatus.PUBLISHED] 
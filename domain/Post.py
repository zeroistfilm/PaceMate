from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum
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

    def soft_delete(self):
        """댓글 소프트 삭제"""
        self.is_deleted = True
        self.content = "삭제된 댓글입니다."

@dataclass
class Attachment:
    id: uuid.UUID               # 첨부파일 ID
    file_name: str              # 파일명
    file_type: str              # 파일 타입
    file_size: int              # 파일 크기
    file_url: str              # 파일 URL
    uploaded_at: datetime       # 업로드 일시

@dataclass
class Product:
    name: str                   # 상품명
    price: float               # 가격
    condition: str             # 상품 상태
    category: str              # 카테고리
    brand: Optional[str] = None  # 브랜드
    model_year: Optional[int] = None  # 모델연도

@dataclass
class Post:
    id: uuid.UUID               # 게시글 ID
    title: str                  # 제목
    content: str                # 내용
    author_id: uuid.UUID        # 작성자 ID
    post_type: PostType         # 게시글 유형
    status: PostStatus          # 상태
    created_at: datetime        # 작성일시
    updated_at: datetime        # 수정일시
    view_count: int = 0         # 조회수
    like_count: int = 0         # 좋아요 수
    comments: List[Comment] = None  # 댓글 목록
    attachments: List[Attachment] = None  # 첨부파일 목록
    product: Optional[Product] = None  # 상품 정보 (중고거래용)
    
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

    def increment_view(self):
        """조회수 증가"""
        self.view_count += 1

    def toggle_like(self) -> bool:
        """좋아요 토글"""
        self.like_count += 1
        return True

    def update_content(self, title: str, content: str):
        """게시글 내용 수정"""
        self.title = title
        self.content = content
        self.updated_at = datetime.now()

    def get_comments_tree(self) -> dict:
        """계층형 댓글 트리 조회"""
        comment_tree = {}
        for comment in self.comments:
            if comment.parent_id is None:
                comment_tree[comment.id] = {
                    'comment': comment,
                    'replies': []
                }
            else:
                if comment.parent_id in comment_tree:
                    comment_tree[comment.parent_id]['replies'].append(comment)
        return comment_tree

    def delete(self):
        """게시글 삭제"""
        self.status = PostStatus.DELETED
        self.updated_at = datetime.now()

    def hide(self):
        """게시글 숨김"""
        self.status = PostStatus.HIDDEN
        self.updated_at = datetime.now()

    def publish(self):
        """게시글 게시"""
        self.status = PostStatus.PUBLISHED
        self.updated_at = datetime.now() 
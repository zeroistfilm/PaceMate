from dataclasses import dataclass
from datetime import datetime
from typing import List
import uuid

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
class Market:
    id: uuid.UUID               # 마켓 ID
    posts: List[MarketPost] = None  # 게시글 목록

    def __post_init__(self):
        if self.posts is None:
            self.posts = []

    def add_post(self, product: Product, seller_id: uuid.UUID) -> MarketPost:
        """게시글 추가"""
        post = MarketPost(
            id=uuid.uuid4(),
            product=product,
            seller_id=seller_id
        )
        self.posts.append(post)
        return post

    def get_active_posts(self) -> List[MarketPost]:
        """활성 게시글 조회"""
        return [post for post in self.posts if post.status == "ACTIVE"] 
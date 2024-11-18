from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class Product:
    id: uuid.UUID               # 상품 ID
    name: str                   # 상품명
    description: str            # 상품 설명
    price: float                # 가격
    condition: str              # 상품 상태 (새것, 중고 등)
    category: str               # 카테고리
    seller_id: uuid.UUID        # 판매자 ID
    created_at: datetime = datetime.now()  # 등록일
    updated_at: datetime = datetime.now()  # 수정일

    def update_price(self, new_price: float):
        """가격 업데이트"""
        self.price = new_price
        self.updated_at = datetime.now()

    def mark_as_sold(self):
        """상품 판매 완료 처리"""
        # 판매 완료 로직 추가 필요
        pass 
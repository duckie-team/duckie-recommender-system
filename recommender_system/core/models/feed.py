# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, VARCHAR, BOOLEAN, DATETIME, String, INT
from core.models.user import User
from core.models import ContentMessage, Category, FeedType


class Feed(BaseModel):
    __tablename__ = "feed"

    """
    @:param
    id: 피드 id
    writer_id: 글쓴이
    type: 글 종류
    is_delete: 삭제 여부
    is_hidden: 숨기기 여부
    content: 텍스트 내용, 사진, 영상
    categories: 카테고리
    create_at: 글 쓴 날짜
    push_count: 끌어올리기 횟수
    lasted_push_at: 언제 마지막으로 끌어올렸는지
    title: 상품명
    price: 가격
    location: 직거래 위치
    is_direct_dealing: 직거래 여부
    parcelable: 택배거래 여부
    deal_state: 거래 상태
    """
    id: Column(String, primary_key=True)
    writer_id: Column(User.nick_name)
    type: FeedType
    is_delete: Column(BOOLEAN, default=False)
    is_hidden: Column(BOOLEAN, default=False)
    content: ContentMessage
    categories: Category
    create_at: Column(DATETIME)
    push_count: Column(INT, default=0)
    lasted_push_at: Column(DATETIME, default=None)
    title: Column(String)
    price: Column(INT)
    location: Optional[Column(String)]
    is_direct_dealing: Column(BOOLEAN, default=False)
    parcelable: Column(BOOLEAN, default=False)
    deal_state: Column(INT, default=0)
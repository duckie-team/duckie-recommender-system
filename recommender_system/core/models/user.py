# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, VARCHAR, BOOLEAN, INT, DATETIME, String
from core.models import Category


class User(BaseModel):
    __tablename__ = "user"

    """
    @:param
    nick_name: 닉네임
    account_enable: 계정 사용 가능 여부
    profile_url: 유저 프로필 이미지 url
    badges: 유저가 획득한 뱃지 번호
    like_category: 좋아하는 분야
    tier: 덕티어
    interested_tags: 관심있는 태그
    non_interested_tags: 관심없는 태그
    trade_preference_tags: 거래하고 싶은 태그
    notification_tags: 태그 알림
    collections: 컬렉션
    create_at: 계정 만든 시간
    delete_at: 계정 삭제한 시간
    banned_at: 밴 당한 시간
    """
    nick_name: Column(VARCHAR(10), primary_key=True, autoincrement=True)
    account_enabled: Column(BOOLEAN)
    profile_url: Column(Column(String))
    like_category: Category
    tier: Column(INT, default=0)
    badges: List[Column(INT, default=0)]
    interested_tags: List[Column(String)]
    non_interested_tags: Optional[List[Column(String, default=None)]]
    trade_preference_tags: Optional[List[Column(String, default=None)]]
    notification_tags: Optional[List[Column(String, default=None)]]
    collections: Optional[List[Column(String, default=None)]]
    create_at: Column(DATETIME)
    delete_at: Optional[Column(DATETIME, default=None)]
    banned_at: Optional[Column(DATETIME, default=None)]
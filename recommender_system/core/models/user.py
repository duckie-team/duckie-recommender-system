# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, VARCHAR, BOOLEAN, TEXT, INT, DATETIME


class Category:
    celebrity: Column(INT=0, message="연애인")
    movie: Column(INT=1, message="영화")
    animation: Column(INT=2, message="만화/애니")
    web_toon: Column(INT=3, message="웹툰")
    game: Column(INT=4, message="게임")
    military: Column(INT=5, message="밀리터리")
    it: Column(INT=6, message="IT")


class User(BaseModel):
    __tablename__ = "user"

    """
    @:param
    nick_name: 닉네임
    account_enable: 계정 사용 가능 여부
    profile_url: 프로필 사진 URL
    like_category: 좋아하는 분야
    interested_tags: 관심있는 태그
    non_interested_tags: 관심없는 태그
    trade_preference_tags: 거래하고 싶은 태그
    create_at: 계정 만든 시간
    """
    nick_name: Column(VARCHAR(10), primary_key=True, autoincrement=True)
    account_enabled: Column(BOOLEAN)
    profile_url: Column(TEXT, nullable=False)
    like_category: Category
    interested_tags: List = [Column(TEXT)]
    non_interested_tags: List = [Column(TEXT)]
    trade_preference_tags: List = [Column(TEXT)]
    create_at: Column(DATETIME)
    delete_at: Optional[Column(DATETIME)]
    banned_at: Optional[Column(DATETIME)]
# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, VARCHAR, BOOLEAN, INT, DATETIME, String


class User(BaseModel):
    __tablename__ = "user"

    class Category:
        celebrity: Column(INT=0, message="연애인")
        movie: Column(INT=1, message="영화")
        animation: Column(INT=2, message="만화/애니")
        web_toon: Column(INT=3, message="웹툰")
        game: Column(INT=4, message="게임")
        military: Column(INT=5, message="밀리터리")
        it: Column(INT=6, message="IT")

    """
    @:param
    nick_name: 닉네임
    account_enable: 계정 사용 가능 여부
    profile_url: 유저 프로필 이미지 url
    badges: 유저가 획득한 뱃지 번호
    like_category: 좋아하는 분야
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
    profile_url: Column(String)
    like_category: Category
    badges: List = [Column(int)]
    interested_tags: List = [Column(String)]
    non_interested_tags: List = [Column(String)]
    trade_preference_tags: List = [Column(String)]
    notification_tags: List = [Column(String)]
    collections: List = [Column(String)]
    create_at: Column(DATETIME)
    delete_at: Optional[Column(DATETIME)]
    banned_at: Optional[Column(DATETIME)]
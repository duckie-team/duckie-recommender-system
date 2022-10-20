# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, String


class Category:
    celebrity: Column(INT=0, message="연애인")
    movie: Column(INT=1, message="영화")
    animation: Column(INT=2, message="만화/애니")
    web_toon: Column(INT=3, message="웹툰")
    game: Column(INT=4, message="게임")
    military: Column(INT=5, message="밀리터리")
    it: Column(INT=6, message="IT")


class ContentMessage(BaseModel):
    """
    @param
    text: 글
    images: 이미지들 url
    video: 영상 url
    """
    text: Column(String)
    images: Optional[List[Column(String)]]
    video: Optional[Column(String)]


class FeedType:
    duck_deal: Column(INT=0, message="덕딜")
    duck_feed: Column(INT=1, message="덕피드")


class Score:
    """
    @:param
    came_feed: 피드 떴을 때
    read: 피드 클릭 안하고 그냥 읽었을 때
    carefully_read: 피드를 클릭해서 자세히 읽었을 때
    heart: 좋아요 눌렀을 때
    write_comment: 댓글을 작성했을 때
    share: 공유 했을 때
    no_interest: 관심 없음
    """
    came_feed = 0
    read = 1
    carefully_read = 2
    heart = 3
    write_comment = 5
    share = 5
    no_interest = -3
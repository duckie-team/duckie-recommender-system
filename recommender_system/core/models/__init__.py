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

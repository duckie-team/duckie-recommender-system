# Import Library
from pydantic import BaseModel
from sqlalchemy import Column, INT
from core.models.user import User
from core.models.feed import Feed
from core.models import Score


class FeedScore(BaseModel):
    __tablename__ = "feed_score"

    """
    @:param
    user_id : 유저 아이디
    feed_id : 피드 아이디
    stay_time : 머문 시간
    score : 점수
    """
    user_id: Column(User.nick_name)
    feed_id: Column(Feed.id)
    stay_time: Column(INT, default=0)
    score: Score
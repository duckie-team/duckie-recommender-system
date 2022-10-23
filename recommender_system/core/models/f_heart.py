# Import Library
from pydantic import BaseModel
from sqlalchemy import Column, String
from core.models.user import User
from core.models.feed import Feed


class FHeart(BaseModel):
    __tablename__ = "f_heart"

    """
    @:param
    target_id: 피드 id
    user_id: 유저 id
    """
    target_id: Column(Feed.id)
    user_id: Column(User.nick_name)
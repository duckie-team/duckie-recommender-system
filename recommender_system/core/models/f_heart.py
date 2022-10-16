# Import Library
from pydantic import BaseModel
from sqlalchemy import Column, String


class FHeart(BaseModel):
    __tablename__ = "f_heart"

    """
    @:param
    feed_id: 피드 id
    user_id: 유저 id
    """
    feed_id: Column(String)
    user_id: Column(String)
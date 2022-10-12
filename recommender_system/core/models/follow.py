# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column
from core.models.user import User


class Follow(BaseModel):
    __tablename__ = "follow"

    """
    @:param
    account_id: 대상 유저 id
    followings: account_id가 팔로우하는 유저들 id
    followers: account_id를 팔로우하는 유저들 id
    blocks: account_id가 차단한 유저들 id 
    """
    account_id: Column(User.nick_name, primary_key=True)
    followings: List = Optional[Column(User.nick_name)]
    followers: List = Optional[Column(User.nick_name)]
    blocks: List = Optional[Column(User.nick_name)]
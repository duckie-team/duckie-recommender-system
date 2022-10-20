# Import Library
from pydantic import BaseModel
from sqlalchemy import Column, INT
from core.models.user import User
from core.models import Category


class TimeCheck(BaseModel):
    __tablename__ = "time_check"

    """
    @:param
    user_id: 유저 아이디
    categories: 키테고리
    search: 검색에 얼마나 머물렀는지
    dm: 디엠창에 얼마나 머물렀는지
    notification: 알림창에 얼마나 머물렀는지
    """
    user_id: Column(User.nick_name)
    categories: Category
    search: Column(INT, default=0)
    dm: Column(INT, default=0)
    notification: Column(INT, default=0)
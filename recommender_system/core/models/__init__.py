# Import Library
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy import Column, String


class ContentMessage(BaseModel):
    text: Column(String)
    images: Optional[List[Column(String)]]
    video: Optional[Column(String)]
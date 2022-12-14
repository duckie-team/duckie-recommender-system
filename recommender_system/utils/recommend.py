# Import Libraries
import pandas as pd
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

# Import Files
from core.models.user import User
from core.models.feed import Feed
from core.models.feed_score import FeedScore
from core.models.f_heart import FHeart
from core.models.time_check import TimeCheck


def dataset_load(session: Session):
    try:
        
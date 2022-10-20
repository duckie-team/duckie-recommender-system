# Import Library
from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

# Import File
# from config import session_score
from utils.recommend import *


router = APIRouter()
print("hello")

@router.get("/")
async def hello():
    return JSONResponse("hello")

@router.get("/recommend", status_code=status.HTTP_200_OK, tags=["recommendation"])
async def recommender(request: Request):
    req_json = await request.json()
    return JSONResponse("hello")
# Import Library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import File
from apps import recommend


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend.router)
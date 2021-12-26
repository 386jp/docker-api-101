import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router

# Load environment variables
load_dotenv()

tags_metadata = [
    {
        "name": "test",
        "description": "APIのテスト用エンドポイント",
    },
    {
        "name": "authors",
        "description": "投稿の著者を管理するAPIエンドポイント",
    },
    {
        "name": "posts",
        "description": "投稿を管理するAPIエンドポイント",
    },
]

app = FastAPI(
    title = "Docker API 101",
    description = "Docker + FastAPI + SQLModel + ReactJS Modern API Example",
    version = "1.0.0",
    openapi_tags=tags_metadata,
    openapi_url = None if os.getenv("DEV_MODE", 'False') == 'False' else '/openapi.json',
    )

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://frontend:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins if os.getenv("DEV_MODE", 'False') == 'False' else ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(router)
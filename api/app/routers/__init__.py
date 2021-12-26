# Import Libraries
from fastapi import APIRouter

# FastAPI settings
router = APIRouter()

# Import routes

from app.routers import api_test
router.include_router(api_test.router)

from app.routers import authors
router.include_router(authors.router)

from app.routers import posts
router.include_router(posts.router)
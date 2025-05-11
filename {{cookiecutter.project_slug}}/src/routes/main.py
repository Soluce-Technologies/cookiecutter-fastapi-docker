from fastapi import APIRouter
from routes.http import welcome

api_router = APIRouter()

# for http
api_router.include_router(welcome.router)

# for ws

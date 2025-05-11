from fastapi import APIRouter
from routes.http import welcome
from routes.ws import linkedin as linkedin_ws

api_router = APIRouter()

# for http
api_router.include_router(welcome.router)

# for ws
api_router.include_router(linkedin_ws.router)
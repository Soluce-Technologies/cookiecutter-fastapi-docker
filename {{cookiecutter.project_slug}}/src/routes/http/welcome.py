from fastapi import APIRouter
from utils.decorators.exceptions import handle_exceptions

router = APIRouter(tags=["welcome"])


@router.get("/")
async def root():
    return {"message": "Hello from {{cookiecutter.project_slug}} API!"}

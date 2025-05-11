from enum import Enum
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv


class Environment(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class Settings(BaseSettings):
    ALLOWED_HOSTS: List[str]
    SECRET_KEY: str  # openssl rand -hex 32
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DEBUG: bool = False

    ENVIRONMENT: Optional[Environment] = "development"

    model_config = SettingsConfigDict(env_file=find_dotenv(), extra="allow")

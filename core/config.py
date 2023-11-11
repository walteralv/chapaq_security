from typing import List
from pydantic import AnyHttpUrl
from decouple import config
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PORT: int = config("PORT", cast=int)
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7   # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:8000"
    ]
    PROJECT_NAME: str = "CHAPAQ"

    #Database
    SQLALCHEMY_DATABASE_URL: str = config("SQLALCHEMY_DATABASE_URL", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()

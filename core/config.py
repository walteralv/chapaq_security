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
    HOST: str = config("HOST", cast=str)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        f"http://0.0.0.0:8000",
        f"http://{HOST}",
        f"http://{HOST}:8000",
    ]
    PROJECT_NAME: str = "CHAPAQ"

    # Database
    SQLALCHEMY_DATABASE_URL: str = config("SQLALCHEMY_DATABASE_URL", cast=str)
    AWS_BUCKET_NAME: str = config("AWS_BUCKET_NAME", cast=str)
    AWS_BUCKET_REGION: str = config("AWS_BUCKET_REGION", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()

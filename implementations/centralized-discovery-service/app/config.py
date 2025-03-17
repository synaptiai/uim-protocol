# app/config.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Configuration settings for the application."""

    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()

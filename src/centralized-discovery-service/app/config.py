# app/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Configuration settings for the application."""
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
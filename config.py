# Configuration file

from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = "/Users/adrianadewunmi/PyCharm/GitHub_Projects/URL-Shortener-FastAPI-Python/.env"


@lru_cache
def get_settings() -> Settings:
    settings: Settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings

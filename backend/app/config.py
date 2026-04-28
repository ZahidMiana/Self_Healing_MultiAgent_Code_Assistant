"""
AgentForge configuration loaded from environment variables.
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = "AgentForge"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    API_V1_PREFIX: str = "/api/v1"

    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "gemini-2.5-flash-preview-04-17"
    GEMINI_MAX_TOKENS: int = 8192
    GEMINI_TEMPERATURE: float = 0.2

    LANGCHAIN_API_KEY: str
    LANGCHAIN_TRACING_V2: str = "true"
    LANGCHAIN_PROJECT: str = "agentforge"

    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USERNAME: str = "neo4j"
    NEO4J_PASSWORD: str

    SECRET_KEY: str
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    WS_HEARTBEAT_INTERVAL: int = 30

    MAX_RETRY_ATTEMPTS: int = 3
    MAX_TASKS_PER_SESSION: int = 8
    EXECUTION_TIMEOUT_SECONDS: int = 30


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

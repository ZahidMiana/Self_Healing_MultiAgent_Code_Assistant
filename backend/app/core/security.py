"""Security helpers for the backend."""

from app.config import settings


def get_cors_origins() -> list[str]:
    return settings.CORS_ORIGINS

"""
Structured logger using Loguru.
"""

import sys
from loguru import logger
from app.config import settings


def setup_logger() -> None:
    logger.remove()

    if settings.ENVIRONMENT == "production":
        logger.add(
            sys.stdout,
            format='{"time":"{time:YYYY-MM-DD HH:mm:ss}","level":"{level}",' \
                   '"module":"{module}","message":"{message}"}',
            level="INFO",
            serialize=True,
        )
    else:
        logger.add(
            sys.stdout,
            format="<green>{time:HH:mm:ss}</green> | <level>{level:<8}</level> | "
                   "<cyan>{module}</cyan> - <level>{message}</level>",
            level="DEBUG",
            colorize=True,
        )

    logger.add(
        "logs/agentforge.log",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        level="INFO",
    )


setup_logger()

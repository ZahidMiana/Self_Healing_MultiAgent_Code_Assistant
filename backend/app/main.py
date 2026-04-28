"""FastAPI application entry point."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.config import settings
from app.core.security import get_cors_origins
from app.database import neo4j_driver
from app.tracing import setup_tracing
from app.api.v1 import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "Starting {name} v{version} [{env}]".format(
            name=settings.APP_NAME,
            version=settings.APP_VERSION,
            env=settings.ENVIRONMENT,
        )
    )
    setup_tracing()
    await neo4j_driver.verify_connectivity()
    await neo4j_driver.create_constraints()
    yield
    await neo4j_driver.close()
    logger.info("AgentForge shutdown complete.")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url=None,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.API_V1_PREFIX, tags=["health"])

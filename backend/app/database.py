"""
Neo4j async driver wrapper.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator
from neo4j import AsyncGraphDatabase, AsyncSession
from loguru import logger
from app.config import settings


class Neo4jDriver:
    def __init__(self) -> None:
        self._driver = AsyncGraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD),
            max_connection_pool_size=50,
        )

    async def verify_connectivity(self) -> None:
        await self._driver.verify_connectivity()
        logger.info("Neo4j connection verified.")

    async def create_constraints(self) -> None:
        async with self._driver.session() as session:
            constraints = [
                "CREATE CONSTRAINT session_id IF NOT EXISTS "
                "FOR (s:Session) REQUIRE s.id IS UNIQUE",
                "CREATE CONSTRAINT task_id IF NOT EXISTS "
                "FOR (t:Task) REQUIRE t.id IS UNIQUE",
            ]
            for cypher in constraints:
                await session.run(cypher)
        logger.info("Neo4j constraints ensured.")

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._driver.session() as s:
            yield s

    async def close(self) -> None:
        await self._driver.close()
        logger.info("Neo4j driver closed.")


neo4j_driver = Neo4jDriver()

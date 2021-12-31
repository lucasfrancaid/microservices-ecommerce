from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.infrastructure.config.settings import static_settings

engine = create_async_engine(static_settings.DATABASE_URL, echo=True)
SessionFactory = sessionmaker(bind=engine, class_=AsyncSession)
Base = declarative_base()


class DatabaseManager:

    @staticmethod
    async def create_database() -> AsyncConnection:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
            return connection

    @staticmethod
    async def drop_database() -> AsyncConnection:
        async with engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            return connection

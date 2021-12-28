from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.infrastructure.config.settings import static_settings

engine = create_async_engine(static_settings.DATABASE_URL, echo=True)
SessionFactory = sessionmaker(bind=engine, class_=AsyncSession)
Base = declarative_base()

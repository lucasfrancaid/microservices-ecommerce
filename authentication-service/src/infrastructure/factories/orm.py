from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.orm.sqlalchemy.database import SessionFactory


class SqlAlchemyFactory:

    @staticmethod
    async def session() -> AsyncSession:
        async with SessionFactory() as session:
            async with session.begin():
                return session

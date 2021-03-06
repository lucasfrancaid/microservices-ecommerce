import pytest
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine
from sqlalchemy.orm import DeclarativeMeta, sessionmaker

from src.infrastructure.factories.orm import SqlAlchemyFactory
from src.infrastructure.orm.sqlalchemy.database import Base, DatabaseManager, engine, SessionFactory


@pytest.mark.sqlalchemy
def test_database_constants():
    assert isinstance(engine, AsyncEngine)
    assert isinstance(SessionFactory, sessionmaker)
    assert isinstance(Base, DeclarativeMeta)


@pytest.mark.sqlalchemy
@pytest.mark.asyncio
async def test_database_manager_create_database():
    connection = await DatabaseManager.create_all()
    session = await SqlAlchemyFactory.session()

    result = await session.execute('SELECT * FROM users;')

    assert isinstance(connection, AsyncConnection)
    assert isinstance(result.fetchall(), list)

    await session.close()
    await connection.close()


@pytest.mark.sqlalchemy
@pytest.mark.asyncio
async def test_database_manager_drop_database():
    connection = await DatabaseManager.drop_all()
    session = await SqlAlchemyFactory.session()

    with pytest.raises(OperationalError) as exc:
        result = await session.execute('SELECT * FROM users')
        result.fetchall()

    assert isinstance(connection, AsyncConnection)
    assert str(exc.value.orig) == 'no such table: users'

    await session.close()
    await connection.close()

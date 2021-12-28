import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.factories.orm import SqlAlchemyFactory


@pytest.mark.asyncio
async def test_sqlalchemy_factory_session():
    session = await SqlAlchemyFactory.session()

    assert isinstance(session, AsyncSession)
    assert session.is_active is True

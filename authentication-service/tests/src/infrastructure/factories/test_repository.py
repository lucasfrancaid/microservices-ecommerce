import pytest

from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.adapters.repositories.authentication_sqlalchemy import AuthenticationRepositorySqlAlchemy
from src.application.repositories.authentication import AuthenticationRepository
from src.infrastructure.config.settings import static_settings
from src.infrastructure.factories.repository import RepositoryFactory


@pytest.mark.asyncio
async def test_repository_factory_make():
    repository = await RepositoryFactory.make()

    assert isinstance(repository, AuthenticationRepository)

    if static_settings.ENVIRONMENT in ('dev', 'prod'):
        assert isinstance(repository, AuthenticationRepositorySqlAlchemy)
    else:
        assert isinstance(repository, AuthenticationRepositoryInMemory)


def test_repository_factory_in_memory():
    repository = RepositoryFactory.in_memory()

    assert isinstance(repository, AuthenticationRepository)
    assert isinstance(repository, AuthenticationRepositoryInMemory)


@pytest.mark.asyncio
async def test_repository_factory_sqlalchemy():
    repository = await RepositoryFactory.sqlalchemy()

    assert isinstance(repository, AuthenticationRepository)
    assert isinstance(repository, AuthenticationRepositorySqlAlchemy)

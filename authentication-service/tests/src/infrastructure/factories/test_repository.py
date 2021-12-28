import pytest

from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.adapters.repositories.authentication_sqlite import AuthenticationRepositorySqlite
from src.application.repositories.authentication import AuthenticationRepository
from src.infrastructure.factories.repository import RepositoryFactory
from src.infrastructure.config.settings import static_settings


@pytest.mark.asyncio
async def test_repository_factory_make():
    repository = await RepositoryFactory.make()

    assert isinstance(repository, AuthenticationRepository)

    if static_settings.ENVIRONMENT in ('dev', 'prod'):
        assert isinstance(repository, AuthenticationRepositorySqlite)
    else:
        assert isinstance(repository, AuthenticationRepositoryInMemory)


def test_repository_factory_in_memory():
    repository = RepositoryFactory.in_memory()

    assert isinstance(repository, AuthenticationRepository)
    assert isinstance(repository, AuthenticationRepositoryInMemory)


@pytest.mark.asyncio
async def test_repository_factory_sqlite():
    repository = await RepositoryFactory.sqlite()

    assert isinstance(repository, AuthenticationRepository)
    assert isinstance(repository, AuthenticationRepositorySqlite)

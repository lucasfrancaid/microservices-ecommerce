from src.application.ports.repositories.authentication import AuthenticationRepository, AuthenticationRepositoryInMemory
from src.infrastructure.factories.repository import RepositoryFactory


def test_repository_factory():
    repository = RepositoryFactory.in_memory()

    assert isinstance(repository, AuthenticationRepository)
    assert isinstance(repository, AuthenticationRepositoryInMemory)

from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.adapters.repositories.authentication_sqlalchemy import AuthenticationRepositorySqlAlchemy
from src.application.repositories.authentication import AuthenticationRepository
from src.infrastructure.config.settings import static_settings
from src.infrastructure.factories.orm import SqlAlchemyFactory


class RepositoryFactory:

    @staticmethod
    async def make() -> AuthenticationRepository:
        repository = await RepositoryFactory.sqlalchemy() \
            if static_settings.ENVIRONMENT in ('dev', 'prod') else RepositoryFactory.in_memory()
        return repository

    @staticmethod
    def in_memory() -> AuthenticationRepositoryInMemory:
        return AuthenticationRepositoryInMemory()

    @staticmethod
    async def sqlalchemy() -> AuthenticationRepositorySqlAlchemy:
        session = await SqlAlchemyFactory.session()
        return AuthenticationRepositorySqlAlchemy(session=session)

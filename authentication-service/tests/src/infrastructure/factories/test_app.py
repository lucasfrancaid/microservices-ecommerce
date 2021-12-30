import pytest

from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.adapters.repositories.authentication_sqlalchemy import AuthenticationRepositorySqlAlchemy
from src.application.repositories.authentication import AuthenticationRepository
from src.application.services.email import EmailService, EmailServiceFake
from src.application.security.password_manager import PasswordManager, PasswordManagerFake
from src.infrastructure.config.settings import static_settings
from src.infrastructure.factories.app import ApplicationFactory, factory_application
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt


def test_application_factory():
    application_factory = ApplicationFactory(
        repository=AuthenticationRepositoryInMemory(),
        email_service=EmailServiceFake(),
        password_manager=PasswordManagerFake()
    )

    assert isinstance(application_factory.repository, AuthenticationRepository)
    assert isinstance(application_factory.email_service, EmailService)
    assert isinstance(application_factory.password_manager, PasswordManager)


@pytest.mark.asyncio
async def test_factory_application():
    factory = await factory_application()

    assert isinstance(factory, ApplicationFactory)
    assert isinstance(factory.email_service, EmailServiceFake)
    assert isinstance(factory.password_manager, PasswordManagerBcrypt)

    if static_settings.ENVIRONMENT in ('dev', 'prod'):
        assert isinstance(factory.repository, AuthenticationRepositorySqlAlchemy)
    else:
        assert isinstance(factory.repository, AuthenticationRepositoryInMemory)

import pytest

from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.adapters.repositories.authentication_sqlalchemy import AuthenticationRepositorySqlAlchemy
from src.application.repositories.authentication import AuthenticationRepository
from src.application.services.email import EmailService, EmailServiceNone
from src.application.security.password_manager import PasswordManager, PasswordManagerNone
from src.application.security.token_manager import TokenManager, TokenManagerNone
from src.infrastructure.config.settings import static_settings
from src.infrastructure.factories.app import ApplicationFactory, factory_application
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt


def test_application_factory():
    application_factory = ApplicationFactory(
        repository=AuthenticationRepositoryInMemory(),
        password_manager=PasswordManagerNone(),
        token_manager=TokenManagerNone(),
        email_service=EmailServiceNone(),
    )

    assert isinstance(application_factory.repository, AuthenticationRepository)
    assert isinstance(application_factory.password_manager, PasswordManager)
    assert isinstance(application_factory.token_manager, TokenManager)
    assert isinstance(application_factory.email_service, EmailService)


def test_application_factory_none():
    application_factory = ApplicationFactory()

    assert application_factory.repository is None
    assert application_factory.password_manager is None
    assert application_factory.token_manager is None
    assert application_factory.email_service is None


@pytest.mark.asyncio
async def test_factory_application():
    factory = await factory_application()

    assert isinstance(factory, ApplicationFactory)
    assert isinstance(factory.password_manager, PasswordManagerBcrypt)
    assert isinstance(factory.token_manager, TokenManagerNone)
    assert isinstance(factory.email_service, EmailServiceNone)

    if static_settings.ENVIRONMENT == 'test':
        assert isinstance(factory.repository, AuthenticationRepositoryInMemory)
    else:
        assert isinstance(factory.repository, AuthenticationRepositorySqlAlchemy)

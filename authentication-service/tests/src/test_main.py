from src.main import ApplicationFactory, factory_application
from src.application.ports.repositories.authentication import AuthenticationRepository, AuthenticationRepositoryInMemory
from src.application.services.email import EmailService, EmailServiceFake
from src.application.security.password_manager import PasswordManager, PasswordManagerFake
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt


def test_aplication_factory():
    application_factory = ApplicationFactory(
        repository=AuthenticationRepositoryInMemory(),
        email_service=EmailServiceFake(),
        password_manager=PasswordManagerFake()
    )

    assert isinstance(application_factory.repository, AuthenticationRepository)
    assert isinstance(application_factory.email_service, EmailService)
    assert isinstance(application_factory.password_manager, PasswordManager)


def test_factory_application():
    factory = factory_application()

    assert isinstance(factory, ApplicationFactory)
    assert isinstance(factory.repository, AuthenticationRepositoryInMemory)
    assert isinstance(factory.email_service, EmailServiceFake)
    assert isinstance(factory.password_manager, PasswordManagerBcrypt)

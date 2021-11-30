from src.application.patterns.factory import Factory
from src.application.ports.repositories.authentication import AuthenticationRepositoryInMemory
from src.application.security.password_manager import PasswordManagerFake
from src.application.services.email import EmailServiceFake


def test_factory_pattern():
    factory = Factory(
        repository=AuthenticationRepositoryInMemory(),
        password_manager=PasswordManagerFake(),
        email_service=EmailServiceFake()
    )

    factory_dir = factory.__dir__()

    assert 'repository' in factory_dir
    assert 'password_manager' in factory_dir
    assert 'email_service' in factory_dir
    assert isinstance(factory.repository, AuthenticationRepositoryInMemory)
    assert isinstance(factory.password_manager, PasswordManagerFake)
    assert isinstance(factory.email_service, EmailServiceFake)

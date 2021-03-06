from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.application.patterns.factory import Factory
from src.application.security.password_manager import PasswordManagerNone
from src.application.services.email import EmailServiceNone


def test_factory_pattern():
    factory = Factory(
        repository=AuthenticationRepositoryInMemory(),
        password_manager=PasswordManagerNone(),
        email_service=EmailServiceNone(),
        another_service=set()
    )

    factory_dir = factory.__dir__()

    assert 'repository' in factory_dir
    assert 'password_manager' in factory_dir
    assert 'email_service' in factory_dir
    assert 'another_service' in factory_dir
    assert isinstance(factory.repository, AuthenticationRepositoryInMemory)
    assert isinstance(factory.password_manager, PasswordManagerNone)
    assert isinstance(factory.email_service, EmailServiceNone)
    assert isinstance(factory.another_service, object)

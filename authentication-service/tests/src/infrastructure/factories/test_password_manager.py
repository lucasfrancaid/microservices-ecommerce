from src.application.security.password_manager import PasswordManager, PasswordManagerFake
from src.infrastructure.factories.password_manager import PasswordManagerFactory


def test_password_manager_factory():
    password_manager = PasswordManagerFactory.fake()

    assert isinstance(password_manager, PasswordManager)
    assert isinstance(password_manager, PasswordManagerFake)

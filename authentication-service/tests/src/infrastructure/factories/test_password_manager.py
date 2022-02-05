from src.application.security.password_manager import PasswordManager, PasswordManagerNone
from src.infrastructure.factories.password_manager import PasswordManagerFactory


def test_password_manager_factory_none():
    password_manager = PasswordManagerFactory.none()

    assert isinstance(password_manager, PasswordManager)
    assert isinstance(password_manager, PasswordManagerNone)

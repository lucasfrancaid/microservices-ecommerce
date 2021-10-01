import pytest

from service.core.security.password_manager import PasswordManager, PasswordManagerNone


def test_password_manager_abstract_class():
    with pytest.raises(NotImplementedError):
        PasswordManager.hash(password=None, salt=None)

    with pytest.raises(NotImplementedError):
        PasswordManager.check(password=None, hashed_password=None)


def test_password_manager_none():
    manager = PasswordManagerNone()

    assert manager.hash(password=None, salt=None) is None
    assert manager.check(password=None, hashed_password=None) is None

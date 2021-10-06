import pytest

from service.core.security.password_manager import PasswordManager, PasswordManagerFake


def test_password_manager_abstract_class():
    with pytest.raises(NotImplementedError):
        PasswordManager.__init__(salt=None)

    with pytest.raises(NotImplementedError):
        PasswordManager.hash(password=None)

    with pytest.raises(NotImplementedError):
        PasswordManager.check(password=None, hashed_password=None)


def test_password_manager_fake():
    manager = PasswordManagerFake(salt=None)

    assert manager.salt is None
    assert manager.hash(password=None) is None
    assert manager.check(password=None, hashed_password=None) is None

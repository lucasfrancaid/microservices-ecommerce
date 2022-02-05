import pytest

from src.application.security.password_manager import PasswordManager, PasswordManagerNone


def test_password_manager_abstract_class():
    PasswordManager.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        PasswordManager().hash()

    with pytest.raises(NotImplementedError):
        PasswordManager().check()


def test_password_manager_none_subclass():
    assert issubclass(PasswordManagerNone, PasswordManager)


def test_password_manager_none_init():
    assert PasswordManagerNone().salt is None


def test_password_manager_none_hash():
    assert PasswordManagerNone().hash(password=None) is None


def test_password_manager_none_check():
    assert PasswordManagerNone().check(password=None, hashed_password=None) is None

import pytest

from src.application.security.password_manager import PasswordManager, PasswordManagerFake


def test_password_manager_abstract_class():
    PasswordManager.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        PasswordManager().hash()

    with pytest.raises(NotImplementedError):
        PasswordManager().check()


def test_password_manager_fake_subclass():
    assert issubclass(PasswordManagerFake, PasswordManager)


def test_password_manager_fake_init():
    assert PasswordManagerFake().salt is None


def test_password_manager_fake_hash():
    assert PasswordManagerFake().hash(password=None) is None


def test_password_manager_fake_check():
    assert PasswordManagerFake().check(password=None, hashed_password=None) is None

import pytest
import bcrypt
from service.core.security.password_manager import PasswordManager

from service.infrastructure.security.bcrypt import PasswordManagerBcrypt

pytest.mock_password = 'Abc123!'
pytest.mock_bcrypt_salt = bcrypt.gensalt()


def test_bcrypt_password_manager_subclass():
    assert issubclass(PasswordManagerBcrypt, PasswordManager)


def test_bcrypt_password_manager_instance_salt():
    password_manager = PasswordManagerBcrypt(salt=pytest.mock_bcrypt_salt)

    assert password_manager.salt == pytest.mock_bcrypt_salt


def test_bcrypt_password_manager_hash_and_check():
    password_manager = PasswordManagerBcrypt(salt=pytest.mock_bcrypt_salt)

    hash_password = password_manager.hash(password=pytest.mock_password)

    assert isinstance(hash_password, bytes)
    assert password_manager.check(password=pytest.mock_password, hash_password=hash_password) is True


def test_bcrypt_password_manager_hash_and_check_different_password_must_be_false():
    wrong_password = 'Xyz456!'
    password_manager = PasswordManagerBcrypt(salt=pytest.mock_bcrypt_salt)

    hash_password = password_manager.hash(password=pytest.mock_password)
    assert password_manager.check(password=wrong_password, hash_password=hash_password) is False


def test_bcrypt_password_manager_check_staticmethod():
    hash_password = PasswordManagerBcrypt(salt=pytest.mock_bcrypt_salt).hash(password=pytest.mock_password)

    assert PasswordManagerBcrypt.check(password=pytest.mock_password, hash_password=hash_password) is True

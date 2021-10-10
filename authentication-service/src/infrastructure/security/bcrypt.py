from typing import Union

import bcrypt

from src.application.security.password_manager import PasswordManager


class PasswordManagerBcrypt(PasswordManager):

    def __init__(self, salt: Union[bytes, str]) -> None:
        self.salt: Union[bytes, str] = salt if isinstance(salt, bytes) else salt.encode()

    def hash(self, password: str) -> bytes:
        hash_password = bcrypt.hashpw(password.encode(), self.salt)
        return hash_password

    @staticmethod
    def check(password: str, hash_password: Union[bytes, str], **kwargs) -> bool:
        encoded_hash_password: bytes = hash_password if isinstance(hash_password, bytes) else hash_password.encode()
        correct_password = bcrypt.checkpw(password.encode(), encoded_hash_password)
        return correct_password

from abc import ABC, abstractmethod
from typing import Union


class PasswordManager(ABC):

    @abstractmethod
    def __init__(salt: Union[bytes, str] = None):
        raise NotImplementedError

    @abstractmethod
    def hash(password: str) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def check(password: str, hashed_password: bytes) -> bool:
        raise NotImplementedError


class PasswordManagerNone(PasswordManager):

    def __init__(self, salt: Union[bytes, str] = None):
        self.salt: Union[bytes, str] = salt

    def hash(self, password: str = None) -> Union[bytes, None]:
        return password.encode() if password else None

    def check(self, password: str = None, hashed_password: bytes = None) -> None:
        pass

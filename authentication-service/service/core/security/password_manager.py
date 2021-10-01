from abc import ABC, abstractmethod
from typing import Union


class PasswordManager(ABC):

    @abstractmethod
    def hash(password: str, salt: Union[bytes, str]) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def check(password: str, hashed_password: bytes) -> bool:
        raise NotImplementedError


class PasswordManagerNone(PasswordManager):

    @staticmethod
    def hash(password: str = None, salt: Union[bytes, str] = None) -> None:
        pass

    @staticmethod
    def check(password: str = None, hashed_password: bytes = None) -> None:
        pass

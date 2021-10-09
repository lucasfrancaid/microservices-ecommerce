from abc import ABC, abstractmethod
from typing import Union


class PasswordManager(ABC):

    @abstractmethod
    def hash(self, password: str = None) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def check(self, password: str = None, hashed_password: bytes = None) -> bool:
        raise NotImplementedError


class PasswordManagerFake(PasswordManager):

    def __init__(self, salt: Union[bytes, str] = None) -> None:
        self.salt: Union[bytes, str] = salt

    def hash(self, password: str = None) -> Union[bytes, None]:
        return password.encode() if password else None

    def check(self, password: str = None, hashed_password: bytes = None) -> None:
        pass

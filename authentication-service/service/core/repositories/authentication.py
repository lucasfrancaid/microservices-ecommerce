from abc import ABC, abstractmethod
from dataclasses import dataclass

from service.core.entities.user import UserEntity


@dataclass
class AuthenticationRepository(ABC):

    @abstractmethod
    def create(entity: UserEntity = None):
        raise NotImplementedError

    @abstractmethod
    def get(user_id: int = None, email: str = None):
        raise NotImplementedError

    @abstractmethod
    def update(user_id: int = None):
        raise NotImplementedError

    @abstractmethod
    def delete(user_id: int = None):
        raise NotImplementedError


class AuthenticationRepositoryNone(AuthenticationRepository):

    @staticmethod
    def create(entity: UserEntity = None):
        pass

    @staticmethod
    def get(user_id: int = None, email: str = None):
        pass

    @staticmethod
    def update(user_id: int = None):
        pass

    @staticmethod
    def delete(user_id: int = None):
        pass

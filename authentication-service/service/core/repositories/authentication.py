from abc import ABC, abstractmethod
from typing import Optional

from service.core.entities.user import UserEntity


class AuthenticationRepository(ABC):

    @abstractmethod
    def create(entity: UserEntity):
        raise NotImplementedError

    @abstractmethod
    def get(user_id: Optional[int] = None, email: Optional[str] = None):
        raise NotImplementedError

    @abstractmethod
    def update(user_id: int):
        raise NotImplementedError

    @abstractmethod
    def delete(user_id: int):
        raise NotImplementedError


class AuthenticationRepositoryNone(AuthenticationRepository):

    @staticmethod
    def create(entity: UserEntity = None):
        pass

    @staticmethod
    def get(user_id: Optional[int] = None, email: Optional[str] = None):
        pass

    @staticmethod
    def update(user_id: int = None):
        pass

    @staticmethod
    def delete(user_id: int = None):
        pass

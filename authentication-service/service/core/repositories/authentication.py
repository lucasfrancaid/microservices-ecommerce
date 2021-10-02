from abc import ABC, abstractmethod
from typing import Optional

from service.core.entities.user import UserEntity
from service.core.entities.repository import RepositoryConfigurationEntity


class AuthenticationRepository(ABC):

    @abstractmethod
    def __init__(configuration: RepositoryConfigurationEntity):
        raise NotImplementedError

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

    def __init__(self, configuration: RepositoryConfigurationEntity = None):
        self.configuration: RepositoryConfigurationEntity = configuration

    def create(self, entity: UserEntity = None):
        return entity 

    def get(self, user_id: Optional[int] = None, email: Optional[str] = None):
        pass

    def update(self, user_id: int = None):
        pass

    def delete(self, user_id: int = None):
        pass

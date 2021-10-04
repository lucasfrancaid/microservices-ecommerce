from abc import ABC, abstractmethod
from typing import Optional, Union

from service.core.entities.user import UserEntity
from service.core.entities.repository import RepositoryConfigurationEntity


class AuthenticationRepository(ABC):

    @abstractmethod
    def __init__(configuration: RepositoryConfigurationEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def create(user_entity: UserEntity) -> Union[UserEntity, None]:
        raise NotImplementedError

    @abstractmethod
    def get(user_id: Optional[int] = None, email: Optional[str] = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    @abstractmethod
    def update(user_id: int, user_entity: UserEntity) -> Union[UserEntity, None]:
        raise NotImplementedError

    @abstractmethod
    def delete(user_id: int) -> bool:
        raise NotImplementedError


class AuthenticationRepositoryNone(AuthenticationRepository):
    user_entity_mock = UserEntity(
        first_name='Lucas',
        last_name='França',
        email='lucas@domain.com',
        hash_password='MyPass123'.encode(),
        confirmation_code=123,
    )

    def __init__(self, configuration: RepositoryConfigurationEntity = None, mock_all: bool = False) -> None:
        self.configuration: RepositoryConfigurationEntity = configuration
        self.mock_all: bool = mock_all

    def create(self, user_entity: UserEntity = None, mock: bool = False) -> Union[UserEntity, None]:
        return self.user_entity_mock if mock or self.mock_all else user_entity

    def get(self, user_id: Optional[int] = None, email: Optional[str] = None, mock: bool = False) -> Union[UserEntity, None]:
        return self.user_entity_mock if mock or self.mock_all else None


    def update(self, user_id: int = None, user_entity: UserEntity = None, mock: bool = False) -> Union[UserEntity, None]:
        return self.user_entity_mock if mock or self.mock_all else user_entity

    def delete(self, user_id: int = None) -> bool:
        pass

from typing import List, Optional, Union
from datetime import datetime

from src.domain.entities.user import UserEntity
from src.application.entities.repository import RepositoryConfigurationEntity
from src.application.interfaces.repository import Repository
from src.application.patterns.singleton import Singleton


class AuthenticationRepository(Repository):

    def all(self, page: int = 1, limit: int = 20) -> List[Optional[UserEntity]]:
        raise NotImplementedError

    def get(self, user_id: Optional[int] = None, email: Optional[str] = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    def create(self, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    def update(self, user_id: int = None, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    def delete(self, user_id: int = None) -> bool:
        raise NotImplementedError


class AuthenticationMemoryStorage(metaclass=Singleton):
    next_id = 0
    data: List[UserEntity] = []

    @classmethod
    def flush(cls):
        cls.next_id = 0
        cls.data = []


class AuthenticationRepositoryInMemory(AuthenticationRepository):

    def __init__(self, configuration: RepositoryConfigurationEntity = None) -> None:
        self.configuration: RepositoryConfigurationEntity = configuration
        self.storage = AuthenticationMemoryStorage()

    def all(self, page: int = 1, limit: int = 20) -> List[Optional[UserEntity]]:
        skip = (page - 1) * limit
        offset = page * limit
        return self.storage.data[skip:offset]

    def get(self, user_id: Optional[int] = None, email: Optional[str] = None) -> Union[UserEntity, None]:
        user = [user for user in self.storage.data if user.user_id == user_id or user.email == email]
        return user[0] if user else None

    def create(self, user_entity: UserEntity) -> Union[UserEntity, None]:
        self.storage.next_id += 1
        user_entity.user_id = self.storage.next_id
        user_entity.confirmation_code = self.storage.next_id    # TODO: Confirmation code is domain of SignUpEntity
        user_entity.created_at = datetime.now()
        self.storage.data.append(user_entity)
        return user_entity

    def update(self, user_id: int, user_entity: UserEntity) -> Union[UserEntity, None]:
        index = [index for index, user in enumerate(self.storage.data) if user.user_id == user_id]
        if not index:
            return None
        self.storage.data[index[0]] = user_entity
        return user_entity

    def delete(self, user_id: int) -> bool:
        index = [index for index, user in enumerate(self.storage.data) if user.user_id == user_id]
        if not index:
            return False
        self.storage.data.pop(index[0])
        return True

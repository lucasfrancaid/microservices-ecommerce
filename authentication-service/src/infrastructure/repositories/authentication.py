from typing import List, Optional, Union

from src.domain.entities.user import UserEntity
from src.application.entities.repository import RepositoryConfigurationEntity
from src.application.ports.repositories.authentication import AuthenticationRepository


class AuthenticationRepositoryPostgres(AuthenticationRepository):

    def __init__(self, configuration: RepositoryConfigurationEntity = None) -> None:
        self.configuration: RepositoryConfigurationEntity = configuration

    def all(self, page: int = 1, limit: int = 20) -> List[Optional[UserEntity]]:
        skip = (page - 1) * limit
        offset = page * limit
        pass

    def get(self, user_id: Optional[int] = None, email: Optional[str] = None) -> Union[UserEntity, None]:
        pass

    def create(self, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        pass

    def update(self, user_id: int = None, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        pass

    def delete(self, user_id: int = None) -> bool:
        pass

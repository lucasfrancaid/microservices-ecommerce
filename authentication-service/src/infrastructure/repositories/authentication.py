from typing import List, Optional, Union

from src.core.domain.entities.user import UserEntity
from src.core.application.entities.repository import RepositoryConfigurationEntity
from src.core.application.ports.repositories.authentication import AuthenticationRepository


class AuthenticationRepositoryPostgres(AuthenticationRepository):

    def __init__(self, configuration: RepositoryConfigurationEntity = None, mock_all: bool = False) -> None:
        self.configuration: RepositoryConfigurationEntity = configuration
        self.mock_all: bool = mock_all

    def all(self, page: int = 1, limit: int = 20) -> List[Optional[UserEntity]]:
        skip = (page - 1) * limit
        offset = page * limit
        return None

    def get(self, user_id: Optional[int] = None, email: Optional[str] = None, mock: bool = False) -> Union[UserEntity, None]:
        pass

    def create(self, user_entity: UserEntity = None, mock: bool = False) -> Union[UserEntity, None]:
        pass

    def update(self, user_id: int = None, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        pass

    def delete(self, user_id: int = None) -> bool:
        pass

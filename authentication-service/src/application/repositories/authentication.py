from typing import List, Optional, Union

from src.application.interfaces.repository import Repository
from src.domain.entities.user import UserEntity


class AuthenticationRepository(Repository):

    async def all(self, page: int = 1, limit: int = 20) -> List[Optional[UserEntity]]:
        raise NotImplementedError

    async def get(self, user_id: Optional[int] = None, email: Optional[str] = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    async def create(self, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    async def update(self, user_id: int = None, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        raise NotImplementedError

    async def delete(self, user_id: int = None) -> bool:
        raise NotImplementedError

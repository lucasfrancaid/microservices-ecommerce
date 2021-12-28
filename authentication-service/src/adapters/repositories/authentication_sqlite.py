from typing import Dict, List, Optional, Union

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.entities.repository import RepositoryConfigurationEntity
from src.application.repositories.authentication import AuthenticationRepository
from src.domain.entities.user import UserEntity
from src.infrastructure.orm.sqlalchemy.models.user import User


class AuthenticationRepositorySqlite(AuthenticationRepository):

    def __init__(self, session: AsyncSession, configuration: RepositoryConfigurationEntity = None) -> None:
        self.session = session
        self.configuration: RepositoryConfigurationEntity = configuration

    async def all(self, page: int = 1, limit: int = 20) -> List[Optional[UserEntity]]:
        query = await self.session.execute(select(User).filter(User.is_active == True))
        users = [UserEntity(**self.__serialize_to_dict(user)) for user in query.scalars().all()]
        return users

    async def get(self, user_id: Optional[int] = None, email: Optional[str] = None) -> Union[UserEntity, None]:
        result = None
        if user_id:
            query = await self.session.get(User, user_id)
            result = query or None
        elif email:
            query = await self.session.execute(select(User).where(User.email == email))
            result = query.scalar_one_or_none()
        user = UserEntity(**self.__serialize_to_dict(result)) if result else None
        return user

    async def create(self, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        user = User(**user_entity.__dict__)
        self.session.add(user)
        await self.session.commit()
        await self.session.flush()
        return user_entity

    async def update(self, user_id: int = None, user_entity: UserEntity = None) -> Union[UserEntity, None]:
        query = update(User).where(User.user_id == user_id)
        query = query.values(**self.__serialize_to_dict_update(user_entity))
        await self.session.execute(query)
        await self.session.commit()
        await self.session.flush()
        return user_entity

    @staticmethod
    def __serialize_to_dict(user: User) -> Dict:
        user_serialize = {**user.__dict__}
        del user_serialize['updated_at']
        del user_serialize['_sa_instance_state']
        return user_serialize

    @staticmethod
    def __serialize_to_dict_update(user_entity: UserEntity) -> Dict:
        user_serialize = {**user_entity.__dict__}
        del user_serialize['user_id']
        del user_serialize['created_at']
        return user_serialize

    async def delete(self, user_id: int = None) -> bool:
        raise NotImplementedError

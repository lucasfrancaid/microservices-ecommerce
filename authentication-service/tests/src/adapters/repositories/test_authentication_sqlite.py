from typing import Dict

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.repositories.authentication_sqlite import AuthenticationRepositorySqlite
from src.application.repositories.authentication import AuthenticationRepository
from src.domain.entities.user import UserEntity

pytest.mock_user_id = None


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_subclass():
    assert issubclass(AuthenticationRepositorySqlite, AuthenticationRepository)


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_init(sqlalchemy_session: AsyncSession):
    repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)

    assert isinstance(repository.session, AsyncSession)
    assert repository.session.is_active is True
    assert repository.configuration is None


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_all(sqlalchemy_session: AsyncSession):
    repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)

    assert isinstance(await repository.all(), list)


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_create(user_entity_dict: Dict, sqlalchemy_session: AsyncSession):
    repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)
    user_entity = UserEntity(**user_entity_dict)
    user_entity.user_id = None
    user_entity.confirmation_code = 123456

    user = await repository.create(user_entity=user_entity)

    assert isinstance(user, UserEntity)
    assert user.first_name == user_entity_dict['first_name']
    assert user.last_name == user_entity_dict['last_name']
    assert user.email == user_entity_dict['email']
    assert user.hash_password == user_entity_dict['hash_password']
    assert user.is_active is False
    assert user.confirmation_code is not None
    assert user.created_at is not None


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_get(user_entity_dict: Dict, sqlalchemy_session: AsyncSession):
    repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)
    user_entity = UserEntity(**user_entity_dict)

    user = await repository.get(email=user_entity.email)

    assert isinstance(user, UserEntity)
    assert user.user_id is not None
    assert user.email == user_entity.email

    pytest.mock_user_id = user.user_id


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_update(user_entity_dict: Dict, sqlalchemy_session: AsyncSession):
    repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)
    user_to_update = UserEntity(**user_entity_dict)
    user_to_update.user_id = pytest.mock_user_id
    user_to_update.confirmation_code = 102030

    user = await repository.update(user_id=user_to_update.user_id, user_entity=user_to_update)

    assert isinstance(user, UserEntity)
    assert user.user_id == user_to_update.user_id
    assert user.confirmation_code == user_to_update.confirmation_code


@pytest.mark.sqlite
@pytest.mark.asyncio
async def test_authentication_repository_sqlite_delete(user_entity_dict: Dict, sqlalchemy_session: AsyncSession):
    repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)
    user_entity = UserEntity(**user_entity_dict)
    user_entity.user_id = pytest.mock_user_id

    has_user_before_delete = await repository.get(user_id=user_entity.user_id)
    assert has_user_before_delete

    with pytest.raises(NotImplementedError):
        await repository.delete(user_id=user_entity.user_id)

    # deleted = await repository.delete(user_id=user_entity.user_id)
    # assert deleted is True
    #
    # has_user_after_delete = await repository.get(user_id=user_entity.user_id)
    # assert has_user_after_delete is None


# @pytest.mark.sqlite
# @pytest.mark.asyncio
# async def test_authentication_repository_sqlite_update_non_existent_user(user_entity_dict: Dict,
#                                                                          sqlalchemy_session: AsyncSession):
#     repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)
#     user_to_update = UserEntity(**user_entity_dict)
#     user_to_update.confirmation_code = 102030
#
#     assert await repository.update(user_id=user_to_update.user_id, user_entity=user_to_update) is None

# @pytest.mark.sqlite
# @pytest.mark.asyncio
# async def test_authentication_repository_sqlite_delete_non_existent_user_must_be_false(
#     user_entity_dict: Dict,
#     sqlalchemy_session: AsyncSession
# ):
#     repository = AuthenticationRepositorySqlite(session=sqlalchemy_session)
#
#     assert await repository.delete(user_id=1232232) is False

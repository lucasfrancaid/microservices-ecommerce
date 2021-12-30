from typing import Dict

import pytest

from src.adapters.repositories.authentication_in_memory import AuthenticationRepositoryInMemory
from src.application.repositories.helpers.authentication import verify_if_user_exists
from src.domain.entities.user import UserEntity


@verify_if_user_exists
async def decorated_function(*args, **kwargs):
    return True


@pytest.mark.asyncio
async def test_verify_if_user_exists(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()
    user_entity = UserEntity(**user_entity_dict)
    repository.storage.data.append(user_entity)

    response = await decorated_function(repository, **{'user_id': user_entity.user_id})

    assert response is True
    repository.storage.flush()


@pytest.mark.asyncio
async def test_verify_if_user_exists_without_authentication_repository_instance_must_return_none():
    response = await decorated_function(**{'user_id': 12302394})

    assert response is None


@pytest.mark.asyncio
async def test_verify_if_user_exists_when_non_exist_must_return_none(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()

    response = await decorated_function(repository, **{'user_id': 12302394})

    assert response is None

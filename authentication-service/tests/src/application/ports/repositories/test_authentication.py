from typing import Dict

import pytest

from src.domain.entities.user import UserEntity
from src.application.interfaces.repository import Repository
from src.application.ports.repositories.authentication import AuthenticationRepository, \
    AuthenticationRepositoryInMemory, AuthenticationMemoryStorage


def test_authentication_repository_abstract_class_is_repository_subclass():
    assert issubclass(AuthenticationRepository, Repository)


def test_authentication_repository_abstract_class():
    AuthenticationRepository.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository().all()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository().get()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository().create()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository().update()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository().delete()


def test_authentication_repository_in_memory_subclass():
    assert issubclass(AuthenticationRepositoryInMemory, AuthenticationRepository)


def test_authentication_repository_in_memory_init():
    repository = AuthenticationRepositoryInMemory()

    assert repository.configuration is None
    assert isinstance(repository.storage, AuthenticationMemoryStorage)


def test_authentication_repository_in_memory_all():
    repository = AuthenticationRepositoryInMemory()

    assert isinstance(repository.all(), list)


def test_authentication_repository_in_memory_get(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()
    user_entity = UserEntity(**user_entity_dict)
    repository.storage.data.append(user_entity)

    user = repository.get(user_id=user_entity.user_id)

    assert isinstance(user, UserEntity)
    assert user.user_id == user_entity.user_id


def test_authentication_repository_in_memory_create(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()
    user_entity = UserEntity(**user_entity_dict)
    user_entity.user_id = None

    user = repository.create(user_entity=user_entity)

    assert isinstance(user, UserEntity)
    assert user.user_id is not None
    assert user.first_name == user_entity_dict['first_name']
    assert user.last_name == user_entity_dict['last_name']
    assert user.email == user_entity_dict['email']
    assert user.hash_password == user_entity_dict['hash_password']
    assert user.is_active is False
    assert user.confirmation_code is not None
    assert user.created_at is not None


def test_authentication_repository_in_memory_update(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()
    user_entity = UserEntity(**user_entity_dict)
    repository.storage.data.append(user_entity)

    user_to_update = UserEntity(**user_entity_dict)
    user_to_update.confirmation_code = 102030
    user = repository.update(user_id=user_to_update.user_id, user_entity=user_to_update)

    assert isinstance(user, UserEntity)
    assert user.user_id == user_to_update.user_id
    assert user.confirmation_code == user_to_update.confirmation_code


def test_authentication_repository_in_memory_delete(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()
    user_entity = UserEntity(**user_entity_dict)
    repository.storage.data.append(user_entity)

    has_user_before_delete = repository.get(user_id=user_entity.user_id)
    assert has_user_before_delete

    deleted = repository.delete(user_id=user_entity.user_id)
    assert deleted is True

    has_user_after_delete = repository.get(user_id=user_entity.user_id)
    assert has_user_after_delete is None


def test_authentication_repository_in_memory_update_non_existent_user(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()

    user_to_update = UserEntity(**user_entity_dict)
    user_to_update.confirmation_code = 102030

    assert repository.update(user_id=user_to_update.user_id, user_entity=user_to_update) is None


def test_authentication_repository_in_memory_delete_non_existent_user_must_be_false(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    repository.storage.flush()

    assert repository.delete(user_id=1232232) is False

from typing import Dict

import pytest

from src.domain.entities.user import UserEntity
from src.application.interfaces.repository import Repository
from src.application.ports.repositories.authentication import AuthenticationRepository, AuthenticationRepositoryInMemory, AuthenticationMemoryStorage


def test_authentication_repository_abstract_class_is_repository_subclass():
    assert issubclass(AuthenticationRepository, Repository)


def test_authentication_repository_abstract_class():
    with pytest.raises(NotImplementedError):
        AuthenticationRepository.__init__(configuration=None)

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.create(user_entity=None)

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.get()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.update(user_id=None, user_entity=None)

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.delete(user_id=None)


def test_authentication_repository_in_memory_subclass():
    assert issubclass(AuthenticationRepositoryInMemory, AuthenticationRepository)


def test_authentication_repository_in_memory_init():
    repository = AuthenticationRepositoryInMemory()

    assert repository.configuration is None
    assert isinstance(repository.storage, AuthenticationMemoryStorage)


def test_authentication_repository_in_memory_all():
    repository = AuthenticationRepositoryInMemory()

    assert isinstance(repository.all(), list)


def test_authentication_repository_in_memory_create(user_entity_dict: Dict):
    repository = AuthenticationRepositoryInMemory()
    user_entity = UserEntity(**user_entity_dict)
    user_entity.user_id = None

    user = repository.create(user_entity=user_entity)

    assert user.user_id is not None
    assert user.first_name == user_entity_dict['first_name']
    assert user.last_name == user_entity_dict['last_name']
    assert user.email == user_entity_dict['email']
    assert user.hash_password == user_entity_dict['hash_password']
    assert user.is_active is False
    assert user.confirmation_code is not None
    assert user.created_at is not None

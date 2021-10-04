import pytest

from service.core.repositories.authentication import AuthenticationRepository, AuthenticationRepositoryNone


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


def test_authentication_repository_none():
    repository = AuthenticationRepositoryNone()

    assert repository.create() is None
    assert repository.get() is None
    assert repository.update() is None
    assert repository.delete() is None

import pytest

from service.core.repositories.authentication import AuthenticationRepository, AuthenticationRepositoryNone


def test_authentication_repository_abstract_class():
    with pytest.raises(NotImplementedError):
        AuthenticationRepository.create()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.get()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.update()

    with pytest.raises(NotImplementedError):
        AuthenticationRepository.delete()


def test_authentication_repository_none():
    repository = AuthenticationRepositoryNone()

    assert repository.create() is None
    assert repository.get() is None
    assert repository.update() is None
    assert repository.delete() is None

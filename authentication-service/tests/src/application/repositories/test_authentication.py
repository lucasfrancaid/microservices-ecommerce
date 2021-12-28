import pytest

from src.application.interfaces.repository import Repository
from src.application.repositories.authentication import AuthenticationRepository


@pytest.mark.asyncio
async def test_authentication_repository_abstract_class_is_repository_subclass():
    assert issubclass(AuthenticationRepository, Repository)


@pytest.mark.asyncio
async def test_authentication_repository_abstract_class():
    AuthenticationRepository.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        await AuthenticationRepository().all()

    with pytest.raises(NotImplementedError):
        await AuthenticationRepository().get()

    with pytest.raises(NotImplementedError):
        await AuthenticationRepository().create()

    with pytest.raises(NotImplementedError):
        await AuthenticationRepository().update()

    with pytest.raises(NotImplementedError):
        await AuthenticationRepository().delete()

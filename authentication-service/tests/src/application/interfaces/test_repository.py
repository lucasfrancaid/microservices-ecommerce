import pytest

from src.application.interfaces.repository import Repository


def test_repository_abstract_class():
    Repository.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        Repository().all()

    with pytest.raises(NotImplementedError):
        Repository().get()

    with pytest.raises(NotImplementedError):
        Repository().create()

    with pytest.raises(NotImplementedError):
        Repository().update()

    with pytest.raises(NotImplementedError):
        Repository().delete()

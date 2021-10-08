import pytest

from src.application.interfaces.usecase import UseCase


def test_use_case_abstract_class():
    with pytest.raises(NotImplementedError):
        UseCase.handler()

    with pytest.raises(NotImplementedError):
        UseCase.serialize()

    with pytest.raises(NotImplementedError):
        UseCase.deserialize()

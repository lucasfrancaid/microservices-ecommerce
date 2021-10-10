import pytest

from src.application.interfaces.controller import Controller


def test_controller_abstract_class():
    Controller.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        Controller().get()

    with pytest.raises(NotImplementedError):
        Controller().post()

    with pytest.raises(NotImplementedError):
        Controller().put()

    with pytest.raises(NotImplementedError):
        Controller().patch()

    with pytest.raises(NotImplementedError):
        Controller().delete()

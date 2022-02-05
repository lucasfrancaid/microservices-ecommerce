import pytest

from src.application.security.token_manager import TokenManager, TokenManagerNone


def test_token_manager_abstract_class():
    TokenManager.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        TokenManager().build()

    with pytest.raises(NotImplementedError):
        TokenManager().refresh()

    with pytest.raises(NotImplementedError):
        TokenManager().validate()

    with pytest.raises(NotImplementedError):
        TokenManager().get_data()


def test_token_manager_none_subclass():
    assert issubclass(TokenManagerNone, TokenManager)


def test_token_manager_none_build():
    assert TokenManagerNone().build(data=None) is None


def test_token_manager_none_refresh():
    assert TokenManagerNone().refresh(refresh_token=None) is None


def test_token_manager_none_validate():
    assert TokenManagerNone().validate(token=None) is None


def test_token_manager_none_get_data():
    assert TokenManagerNone().get_data(token=None) is None

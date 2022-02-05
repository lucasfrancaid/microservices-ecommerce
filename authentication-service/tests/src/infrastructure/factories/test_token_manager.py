from src.application.security.token_manager import TokenManager, TokenManagerNone
from src.infrastructure.factories.token_manager import TokenManagerFactory


def test_password_manager_factory_none():
    token_manager = TokenManagerFactory.none()

    assert isinstance(token_manager, TokenManager)
    assert isinstance(token_manager, TokenManagerNone)

from src.infrastructure.config.settings import Settings, static_settings


def test_static_settings():
    assert isinstance(static_settings, Settings)

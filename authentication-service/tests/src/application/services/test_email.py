import pytest

from src.application.services.email import EmailService, EmailServiceNone


def test_email_service_abstract_class():
    EmailService.__abstractmethods__ = set()

    with pytest.raises(NotImplementedError):
        EmailService().send()


def test_email_service_none():
    provider = EmailServiceNone()

    assert provider.configuration is None
    assert provider.send(email_entity=None) is None

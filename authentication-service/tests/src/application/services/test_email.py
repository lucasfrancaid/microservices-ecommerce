import pytest

from src.application.services.email import EmailService, EmailServiceFake


def test_email_service_abstract_class():
    with pytest.raises(NotImplementedError):
        EmailService.__init__(configuration=None)

    with pytest.raises(NotImplementedError):
        EmailService.send(email_entity=None)


def test_email_service_fake():
    provider = EmailServiceFake()

    assert provider.configuration is None
    assert provider.send(email_entity=None) is None

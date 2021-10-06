import pytest

from service.core.providers.email import EmailProvider, EmailProviderFake


def test_email_abstract_class():
    with pytest.raises(NotImplementedError):
        EmailProvider.__init__(configuration=None)

    with pytest.raises(NotImplementedError):
        EmailProvider.send(email_entity=None)

def test_email_fake():
    provider = EmailProviderFake()

    assert provider.configuration is None
    assert provider.send(email_entity=None) is None

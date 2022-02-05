from src.application.services.email import EmailService, EmailServiceNone
from src.infrastructure.factories.email_service import EmailServiceFactory


def test_email_service_factory_none():
    email_service = EmailServiceFactory.none()

    assert isinstance(email_service, EmailService)
    assert isinstance(email_service, EmailServiceNone)

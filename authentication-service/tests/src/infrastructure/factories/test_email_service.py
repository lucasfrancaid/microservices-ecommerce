from src.application.services.email import EmailService, EmailServiceFake
from src.infrastructure.factories.email_service import EmailServiceFactory


def test_email_service_factory():
    email_service = EmailServiceFactory.fake()

    assert isinstance(email_service, EmailService)
    assert isinstance(email_service, EmailServiceFake)

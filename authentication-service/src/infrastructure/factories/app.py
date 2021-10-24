from src.application.ports.repositories.authentication import AuthenticationRepository
from src.application.security.password_manager import PasswordManager
from src.application.services.email import EmailService

from src.infrastructure.factories.email_service import EmailServiceFactory
from src.infrastructure.factories.password_manager import PasswordManagerFactory
from src.infrastructure.factories.repository import RepositoryFactory


class ApplicationFactory:

    def __init__(
        self, repository: AuthenticationRepository, password_manager: PasswordManager, email_service: EmailService
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager
        self.email_service: EmailService = email_service


def factory_application() -> ApplicationFactory:
    factory = ApplicationFactory(
        repository=RepositoryFactory.in_memory(),
        password_manager=PasswordManagerFactory.bcrypt(),
        email_service=EmailServiceFactory.fake()
    )
    return factory

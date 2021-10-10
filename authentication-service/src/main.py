import bcrypt

from src.application.ports.repositories.authentication import AuthenticationRepository, AuthenticationRepositoryInMemory
from src.application.security.password_manager import PasswordManager
from src.application.services.email import EmailService, EmailServiceFake
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt

PASSWORD_SALT = bcrypt.gensalt()


class ApplicationFactory():

    def __init__(
        self, repository: AuthenticationRepository, password_manager: PasswordManager, email_service: EmailService
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager
        self.email_service: EmailService = email_service


def factory_application() -> ApplicationFactory:
    factory = ApplicationFactory(
        repository=AuthenticationRepositoryInMemory(),
        password_manager=PasswordManagerBcrypt(salt=PASSWORD_SALT),
        email_service=EmailServiceFake()
    )
    return factory

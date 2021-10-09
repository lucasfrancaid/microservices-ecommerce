import bcrypt

from src.application.ports.repositories.authentication import AuthenticationRepository, \
    AuthenticationRepositoryInMemory
from src.application.security.password_manager import PasswordManager
from src.application.services.email import EmailService, EmailServiceFake
from src.infrastructure.security.bcrypt import PasswordManagerBcrypt


class FactoryApplication:

    def __init__(
        self,
        repository: AuthenticationRepository,
        password_manager: PasswordManager,
        email_service: EmailService
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager
        self.email_service: EmailService = email_service

    def run(self):
        raise NotImplementedError


if __name__ == '__main__':
    factory = FactoryApplication(
        repository=AuthenticationRepositoryInMemory(),
        password_manager=PasswordManagerBcrypt(salt=bcrypt.gensalt()),
        email_service=EmailServiceFake()
    )
    factory.run()

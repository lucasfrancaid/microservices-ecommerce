from src.application.repositories.authentication import AuthenticationRepository
from src.application.security.password_manager import PasswordManager
from src.application.security.token_manager import TokenManager
from src.application.services.email import EmailService
from src.infrastructure.factories.email_service import EmailServiceFactory
from src.infrastructure.factories.password_manager import PasswordManagerFactory
from src.infrastructure.factories.repository import RepositoryFactory
from src.infrastructure.factories.token_manager import TokenManagerFactory


class ApplicationFactory:

    def __init__(
        self,
        repository: AuthenticationRepository = None,
        password_manager: PasswordManager = None,
        token_manager: TokenManager = None,
        email_service: EmailService = None
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager
        self.token_manager: TokenManager = token_manager
        self.email_service: EmailService = email_service


async def factory_application() -> ApplicationFactory:
    factory = ApplicationFactory(
        repository=await RepositoryFactory.make(),
        password_manager=PasswordManagerFactory.bcrypt(),
        token_manager=TokenManagerFactory.none(),
        email_service=EmailServiceFactory.none()
    )
    return factory

from src.application.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from src.application.interfaces.controller import Controller
from src.application.ports.repositories.authentication import AuthenticationRepository
from src.application.security.password_manager import PasswordManager
from src.application.services.email import EmailService
from src.application.usecases.sign_up import SignUpUseCase, SignUpConfirmationAccountUseCase


class SignUpController(Controller):

    @staticmethod
    def post(repository: AuthenticationRepository, password_manager: PasswordManager, email_service: EmailService,
             entity: SignUpEntity):
        use_case = SignUpUseCase(
            repository=repository,
            password_manager=password_manager,
            email_service=email_service,
        )
        response = use_case.handler(entity=entity)
        return response

    @staticmethod
    def put(repository: AuthenticationRepository, email_service: EmailService, entity: SignUpConfirmationAccountEntity):
        use_case = SignUpConfirmationAccountUseCase(
            repository=repository,
            email_service=email_service,
        )
        response = use_case.handler(confirmation_entity=entity)
        return response

    def get(self):
        raise NotImplementedError

    def patch(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

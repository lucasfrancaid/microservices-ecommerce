from typing import Dict

from service.core.entities.email import SendEmailEntity
from service.core.entities.sign_up import SignUpEmailEntity, SignUpEntity, SignUpConfirmationEntity
from service.core.entities.user import UserEntity
from service.core.providers.email import EmailProvider
from service.core.repositories.authentication import AuthenticationRepository
from service.core.security.password_manager import PasswordManager


class SignUpUseCase:

    def __init__(
        self,
        repository: AuthenticationRepository,
        password_manager: PasswordManager,
        email_provider: EmailProvider,
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager
        self.email_provider: EmailProvider = email_provider

    def check_if_email_is_available(self, email_entity: SignUpEmailEntity) -> bool:
        user = self.repository.get(email=email_entity.email)
        return True if user else False

    def handler(self, entity: SignUpEntity) -> Dict:
        serialized_user = self.serialize(entity=entity)
        user_entity = self.user_register(user_entity=serialized_user)
        self.send_email(user_entity)
        return user_entity.dict()

    def serialize(self, entity: SignUpEntity) -> UserEntity:
        delimiter = ' '
        first_name, *last_name = entity.full_name.split(delimiter)
        hash_password = self.password_manager.hash(password=entity.password)
        user_entity = UserEntity(
            first_name=first_name,
            last_name=delimiter.join(last_name),
            email=entity.email,
            hash_password=hash_password
        )
        return user_entity

    def user_register(self, user_entity: UserEntity) -> UserEntity:
        registered_user = self.repository.create(entity=user_entity)
        return registered_user

    def send_email(self, user_entity: UserEntity) -> None:
        send_email_entity = SendEmailEntity(
            subject='Your new account',
            email_from='from_root@root.com',
            email_to=[user_entity.email],
            body='Your new account'
        )
        self.email_provider.send(email_entity=send_email_entity)

    def confirmation_account(self, confirmation_entity: SignUpConfirmationEntity) -> UserEntity:
        user = self.repository.get(email=confirmation_entity.email)

        if not user.confirmation_code == confirmation_entity.confirmation_code:
            raise ValueError('Confirmation code must be equal')
        
        user.is_active = True
        updated_user = self.repository.update(user)
        return updated_user

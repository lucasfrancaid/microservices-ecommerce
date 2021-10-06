from typing import Dict

from service.core.usecases import UseCase
from service.core.entities.email import SendEmailEntity
from service.core.entities.sign_up import SignUpEntity, SignUpConfirmationAccountEntity
from service.core.entities.user import UserEntity
from service.core.providers.email import EmailProvider
from service.core.repositories.authentication import AuthenticationRepository
from service.core.security.password_manager import PasswordManager


class SignUpUseCase(UseCase):

    def __init__(
        self,
        repository: AuthenticationRepository,
        password_manager: PasswordManager,
        email_provider: EmailProvider,
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.password_manager: PasswordManager = password_manager
        self.email_provider: EmailProvider = email_provider

    def handler(self, entity: SignUpEntity) -> Dict:
        email_is_available = self.check_if_email_is_available(email=entity.email)

        if not email_is_available:
            raise Exception('email is not available')

        serialized_user = self.serialize(entity=entity)
        user_entity = self.user_register(user_entity=serialized_user)
        self.send_email(user_entity)

        deserialized_user = self.deserialize(user_entity=user_entity)
        return deserialized_user

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

    def deserialize(self, user_entity: UserEntity):
        return user_entity.dict()

    def check_if_email_is_available(self, email: str) -> bool:
        user = self.repository.get(email=email)
        return not user or not user.is_active

    def user_register(self, user_entity: UserEntity) -> UserEntity:
        registered_user = self.repository.create(user_entity=user_entity)
        return registered_user

    def send_email(self, user_entity: UserEntity) -> None:
        send_email_entity = SendEmailEntity(
            subject='Your new account',
            email_from='from_root@root.com',
            email_to=[user_entity.email],
            body='Your new account'
        )
        self.email_provider.send(email_entity=send_email_entity)


class SignUpConfirmationAccountUseCase(UseCase):

    def __init__(
        self,
        repository: AuthenticationRepository,
        email_provider: EmailProvider,
    ) -> None:
        self.repository: AuthenticationRepository = repository
        self.email_provider: EmailProvider = email_provider

    def handler(self, confirmation_entity: SignUpConfirmationAccountEntity) -> Dict:
        user = self.repository.get(email=confirmation_entity.email)

        if not user.confirmation_code == confirmation_entity.confirmation_code:
            raise ValueError('incorrect confirmation code')

        user.is_active = True
        updated_user = self.repository.update(user_id=user.user_id, user_entity=user)

        deserialized_user = self.deserialize(user_entity=updated_user)
        return deserialized_user

    def serialize(*args, **kwargs):
        raise NotImplementedError

    def deserialize(self, user_entity: UserEntity) -> Dict:
        return user_entity.dict()
